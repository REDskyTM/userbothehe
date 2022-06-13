from pyrogram import Client, filters
from pyrogram import types

from PIL import Image, ImageDraw, ImageFont, ImageChops
import imageio
import requests
import io, os, sys
try:
    import lottie
    from lottie.importers.core import import_tgs
    from lottie.importers.raster import import_raster

    from lottie.exporters.gif import export_gif
    from lottie.exporters.core import export_tgs

except Exception as e:
    lottie = None
    import warnings
    warnings.warn(repr(e))




__module_info__ = {
    'name': {
        'en': 'Demotivator',
        'ru': 'Демотиватор'
    },
    'author': ['pelmeshke', '@pelmeshke'],
    'version': 'v1.1',
    'description': {
        'en': 'Creates demotivator from photo with caption (try it yourself to understand). Also creates "slavik meme"',
        'ru': 'Создаёт демотиватор из фото с подписью (попробуйте сами, чтобы понять). Также создает "мем славика".'
    },
    'commands': {
        '.demot': {
            'desc': {
                'en': 'Creating demotivator. As photo also takes gifs, stickers, video or user\'s photo. As caption takes text in command or photo\'s caption',
                'ru': 'Создает демотиватор. В качестве фото берет гифки, стикеры, видео или фото пользователя. В качестве подписи берет текст в команде или подпись фото'
            },
            'func': 'command([\'demot\'], \'.\')'
        },
        '.slavik': {
            'desc': {
                'en': 'Creating slavik meme. As photo also takes gifs, stickers, video or user\'s photo. As caption takes text in command or photo\'s caption',
                'ru': 'Создает мем славика. В качестве фото берет гифки, стикеры, видео или фото пользователя. В качестве подписи берет текст в команде или подпись фото'
            },
            'func': 'command([\'slavik\'], \'.\')'
        },

    },
    'dependencies': ['PIL (or Python Image Library)', 'requests (for fonts)', 'imageio (to convert .mp4 to .gif)', 'lottie (to convert .tgs to .gif)'],
    'requirements': [],
    'changelog': {
        'v1.1': {
            'en': 'Added the able to create demotivator from animated sticker.',
            'ru': 'Добавлена возможность создавать демотиваторы из анимированных стикеров.'
        }
    },
}


# for KGBot
class Main:
    in_help = '.demot, .slavik'
    cmd_list = '.demot, .slavik'.split(', ')
    ver = 'v1.1'
    des = f'Создаёт демотиватор из фото с подписью (попробуйте сами, чтобы понять). ' + \
    'Также создает "мем славика". Создано @pelmeshke.\nЗависимости: {", ".join(__module_info__["dependencies"])}.\n\n' + \
    'Список изменений (v1.1): \n    Добавлена возможность создавать демотиваторы из анимированных стикеров.'

    

LOBSTER_FONT = requests.get('https://github.com/pelmesh619/fonts/blob/main/Lobster.ttf?raw=true').content
TIMESNEWROMAN_FONT = requests.get('https://github.com/pelmesh619/fonts/blob/main/TimesNewRoman.ttf?raw=true').content



@Client.on_message(filters.me & filters.reply & filters.command('demot', '.'))
async def demotivator_handler(peluserbot, message):
    photo = get_media(message.reply_to_message)

    await message.edit_text('🔄<b>Скачиваю фото</b>🔄')
    photo_path = await peluserbot.download_media(photo)

    caption = ' '.join(message.text.split(' ')[1:]) or \
              message.reply_to_message.text or \
              message.reply_to_message.caption or \
              'ГДЕ ПОДПИСЬ, БЛЯДЬ!!!'

    await message.edit_text('🔄<b>Фотожоплю</b>🔄')

    if photo_path.lower().endswith('.tgs'):
        gif_path = await convert_tgs_to_gif(photo_path)
        out = await demotivator_gif(gif_path, caption)
        os.remove(photo_path)
        photo_path = gif_path
    elif photo_path.lower().endswith('.mp4'):
        gif_path = await convert_mp4_to_gif(photo_path)
        out = await demotivator_gif(gif_path, caption)
        os.remove(photo_path)
        photo_path = gif_path
    elif photo_path.lower().endswith('.gif'):
        out = await demotivator_gif(photo_path, caption)
    else:
        out = await demotivator(photo_path, caption)


    

    await message.edit_text('🔄<b>Отправляю</b>🔄')
    if photo_path.lower().endswith('.gif'):
        await message.reply_to_message.reply_animation(out, duration=getattr(photo, 'duration', 0))
    else:
        await message.reply_to_message.reply_photo(out)

    await message.delete()
    os.remove(photo_path)



@Client.on_message(filters.me & filters.reply & filters.command('slavik', '.'))
async def slavik_handler(peluserbot, message):
    photo = get_media(message.reply_to_message)

    await message.edit_text('🔄<b>Скачиваю фото</b>🔄')
    photo_path = await peluserbot.download_media(photo)

    try:
        caption = ' '.join(message.text.split(' ')[1:]) or \
                  message.reply_to_message.text or \
                  message.reply_to_message.caption or \
                  'ГДЕ ПОДПИСЬ, БЛЯДЬ!!!'

        await message.edit_text('🔄<b>Фотожоплю</b>🔄')

        if photo_path.lower().endswith('.tgs'):
            gif_path = await convert_tgs_to_gif(photo_path)
            out = await slavik_gif(gif_path, caption)
            os.remove(photo_path)
            photo_path = gif_path
        if photo_path.lower().endswith('.mp4'):
            gif_path = await convert_mp4_to_gif(photo_path)
            out = await slavik_gif(gif_path, caption)
            os.remove(photo_path)
            photo_path = gif_path
        elif photo_path.lower().endswith('.gif'):
            out = await slavik_gif(photo_path, caption)
        else:
            out = await slavik(photo_path, caption)


        

        await message.edit_text('🔄<b>Отправляю</b>🔄')
        if photo_path.lower().endswith('.gif'):
            await message.reply_to_message.reply_animation(out, duration=getattr(photo, 'duration', 0))
        else:
            await message.reply_to_message.reply_photo(out)

        await message.delete()
    finally:
        os.remove(photo_path)



def get_media(message):
    return message.photo or \
           message.sticker and not message.sticker.is_animated and message.sticker or \
           message.sticker and lottie and message.sticker.is_animated and message.sticker or \
           message.animation or message.video or message.video_note or \
           message.document and \
           (message.document.file_name.lower().endswith('.gif') or \
           message.document.file_name.lower().endswith('.jpg') or \
           message.document.file_name.lower().endswith('.png') or \
           message.document.file_name.lower().endswith('.jpeg') or \
           message.document.file_name.lower().endswith('.webp') or \
           message.document.file_name.lower().endswith('.tgs') or \
           message.document.file_name.lower().endswith('.mp4')) and \
           message.document or \
           message.forward_from and \
           message.forward_from.photo.big_file_id or \
           message.from_user.photo.big_file_id



# Size of demotivator picture
SIZE = (1536, 1536)
# Size of demotivator gif
GIF_SIZE = (360, 360)

async def demotivator(path, caption):
    image = Image.open(path)

    black_image = Image.new('RGB', SIZE, (0, 0, 0))

    image = image.resize((int(SIZE[0]*.8), int(SIZE[1]*.7)))

    black_image.paste(image, (int(SIZE[0]*.1), int(SIZE[1]*0.05)))

    txt = Image.new("RGB", black_image.size, (0, 0, 0))

    font = ImageFont.truetype(io.BytesIO(TIMESNEWROMAN_FONT), SIZE[1]//20)


    d = ImageDraw.Draw(txt)

    text_xy = d.multiline_textsize(caption, font=font)
    text_xy = (SIZE[0] - text_xy[0]) // 2, (SIZE[1]*0.25 - text_xy[1]) // 2 + SIZE[1]*0.75


    d.multiline_text(text_xy, caption, font=font, fill=(255, 255, 255), align='center')

    lines_xy = (
        int(SIZE[0]*.1 - SIZE[0]*.01), 
        int(SIZE[0]*.9 + SIZE[0]*.01), 
        int(SIZE[1]*0.05 - SIZE[1]*0.01), 
        int(SIZE[1]*0.75 + SIZE[1]*0.01),
    )

    d.line(((lines_xy[0], lines_xy[2]), (lines_xy[0], lines_xy[3])), width=int(SIZE[0]*.005))
    d.line(((lines_xy[1], lines_xy[2]), (lines_xy[1], lines_xy[3])), width=int(SIZE[0]*.005))
    d.line(((lines_xy[0], lines_xy[2]), (lines_xy[1], lines_xy[2])), width=int(SIZE[0]*.005))
    d.line(((lines_xy[0], lines_xy[3]), (lines_xy[1], lines_xy[3])), width=int(SIZE[0]*.005))

    out = ImageChops.add(black_image, txt)

    output = io.BytesIO()
    output.name = 'demot.png'
    out.save(output, "PNG")
    output.seek(0)

    print('done')
    return output


async def demotivator_gif(path, caption):
    gif = Image.open(path)
    print(path, gif.format, gif.is_animated, gif.tell(), gif.tell(), gif.n_frames, gif.size)


    font = ImageFont.truetype(io.BytesIO(TIMESNEWROMAN_FONT), GIF_SIZE[1]//20)

    images = []

    black_image = Image.new('RGBA', GIF_SIZE, (0, 0, 0))
    txt = Image.new("RGBA", black_image.size, (0, 0, 0))
    d = ImageDraw.Draw(txt)

    text_xy = d.multiline_textsize(caption, font=font)
    text_xy = (GIF_SIZE[0] - text_xy[0]) // 2, (GIF_SIZE[1]*0.25 - text_xy[1]) // 2 + GIF_SIZE[1]*0.75


    lines_xy = (
        int(GIF_SIZE[0]*.1 - GIF_SIZE[0]*.01), 
        int(GIF_SIZE[0]*.9 + GIF_SIZE[0]*.01), 
        int(GIF_SIZE[1]*0.05 - GIF_SIZE[1]*0.01), 
        int(GIF_SIZE[1]*0.75 + GIF_SIZE[1]*0.01),
    )
    d.multiline_text(text_xy, caption, font=font, fill=(255, 255, 255), align='center')

    d.line(((lines_xy[0], lines_xy[2]), (lines_xy[0], lines_xy[3])), width=int(GIF_SIZE[0]*.005))
    d.line(((lines_xy[1], lines_xy[2]), (lines_xy[1], lines_xy[3])), width=int(GIF_SIZE[0]*.005))
    d.line(((lines_xy[0], lines_xy[2]), (lines_xy[1], lines_xy[2])), width=int(GIF_SIZE[0]*.005))
    d.line(((lines_xy[0], lines_xy[3]), (lines_xy[1], lines_xy[3])), width=int(GIF_SIZE[0]*.005))


    for i in range(gif.n_frames):
        gif.seek(i)
        image = gif.convert('RGBA')
        image = image.resize((int(GIF_SIZE[0]*.8), int(GIF_SIZE[1]*.7)))

        black_image_copy = black_image.copy()
        black_image_copy.paste(image, (int(GIF_SIZE[0]*.1), int(GIF_SIZE[1]*0.05)))

        out = ImageChops.add(black_image_copy, txt)
        # if i % 100 == 0:
        #     out.show()

        images.append(out)





    out = io.BytesIO()
    out.name = 'demot.gif'
    images[0].save(out, 'GIF', save_all=True, append_images=images[1:], optimize=True)
    out.seek(0)

    print('done')
    return out





async def slavik(path, caption):
    image = Image.open(path)
    d = ImageDraw.Draw(image)

    
    i = image.size[1]//12
    while i > 0:
        font = ImageFont.truetype(io.BytesIO(LOBSTER_FONT), i)
        text_xy = d.multiline_textsize(caption, font=font)

        if text_xy[0] < image.size[0] * .9:
            break
        i -= 2

    text_xy = (image.size[0] - text_xy[0]) // 2, image.size[1] - image.size[1] // 8
    d.multiline_text((text_xy[0]+1, text_xy[1]+1), caption, font=font, fill=(0, 0, 0), align='center')
    d.multiline_text(text_xy, caption, font=font, fill=(255, 255, 255), align='center')


    out = io.BytesIO()
    out.name = 'slavik.png'
    image.save(out, "PNG")
    out.seek(0)


    print('done')
    return out





async def slavik_gif(path, caption):
    gif = Image.open(path)
    size = gif.size


    images = []

    for i in range(gif.n_frames):
        gif.seek(i)
        image = gif.convert('RGBA')


        d = ImageDraw.Draw(image)
        if i == 0:
            j = size[1]//10
            while j > 0:
                font = ImageFont.truetype(io.BytesIO(LOBSTER_FONT), j)
                text_xy = d.multiline_textsize(caption, font=font)

                if text_xy[0] < size[0] * .9:
                    break
                j -= 2

            text_xy = (size[0] - text_xy[0]) // 2, size[1] - size[1] // 7
        d.multiline_text((text_xy[0]+1, text_xy[1]+1), caption, font=font, fill=(0, 0, 0), align='center')
        d.multiline_text(text_xy, caption, font=font, fill=(255, 255, 255), align='center')

        images.append(image)


    out = io.BytesIO()
    out.name = 'slavik.gif'
    images[0].save(out, 'GIF', save_all=True, append_images=images[1:], optimize=True)
    out.seek(0)


    print('done')
    return out



# Converts mp4 to gif
async def convert_mp4_to_gif(inputpath):
    """Reference: http://imageio.readthedocs.io/en/latest/examples.html#convert-a-movie"""
    outputpath = os.path.splitext(inputpath)[0] + '.gif'

    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputpath, fps=fps)
    for i,im in enumerate(reader):
        writer.append_data(im)
    writer.close()
    return outputpath


async def convert_tgs_to_gif(file_path):
    anim = import_tgs(file_path)
    export_gif(anim, file_path.rstrip('.tgs')+'.gif')

    return file_path.rstrip('.tgs')+'.gif'




