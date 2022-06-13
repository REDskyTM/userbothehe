from pyrogram import Client, filters
import os
import speedtestos.popen("pip install speedtest")

import speedtest


@Client.on_message(filters.me & filters.command('speedtest', '.'))
async def speedtest_handler(peluserbot, message):
	st = speedtest.Speedtest()
	await message.edit('Testing...')

	download = st.download()
	upload = st.upload()

	servernames = []
	st.get_servers(servernames)
	ping = st.results.ping

	await message.edit(
		'Results:\n\nPing: {} ms\nDownload: {}\nUpload: {}\n'.format(
			ping, 
			memory_to_string(download), 
			memory_to_string(upload)
		)
	)



def memory_to_string(memory, lang_code='en'):
    sizes = ['bps', "kbps", "Mbps", "Gbps"]
    count = 0
    while memory > 1024 and count < len(sizes):
        memory /= 1024
        count += 1

    return str(round(memory, 2)) + ' ' + sizes[count]

