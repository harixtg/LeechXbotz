YT_HELP_MESSAGE = """
<b>To use the commands, follow this format:</b>
<code>/{cmd} link options</code> or replying to link </b>
<code>/{cmd} options</code>

<b>OPTIONS:</b>
<b>-s:</b> Select quality for specific link or links.

<b>-z password:</b> Create a password-protected zip file.

<b>-n new_name:</b> Rename the file.

<b>-t thumbnail url:</b> Custom thumbnail for each leexh.(raw or tg image url)

<b>-ss value:</b> Generate ss for leech video, max 10 for each leach.

<b>-id drive_folder_link or drive_id -index https://anything.in/0:</b> Upload to a custom drive.

<b>-opt playliststart:^10|fragment_retries:^inf|matchtitle:S13|writesubtitles:true|live_from_start:true|postprocessor_args:{{"ffmpeg": ["-threads", "4"]}}|wait_for_video:(5, 100):</b> Set additional options.

<b>-i 10:</b> Process multiple links.

<b>-b:</b> Perform bulk download by replying to a text message or file with links separated with new line.


<b>Check all yt-dlp api options from this <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FILE</a> or use this <a href='https://t.me/mltb_official_channel/177'>script</a> to convert cli arguments to api options.</b>
"""

MIRROR_HELP_MESSAGE = """
<b>ᴛᴏ ᴜꜱᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅꜱ, ғᴏʟʟᴏᴡ ᴛʜɪꜱ ғᴏʀᴍᴀᴛ:</b>

<code>/{cmd} link options</code> or replying to link </b>
<code>/{cmd} options</code>

<b>𝗢𝗣𝗧𝗜𝗢𝗡𝗦 :</b>

<b>-n new name:</b> Rᴇɴᴀᴍᴇ ᴛʜᴇ ғɪʟᴇ ᴏʀ ғᴏʟᴅᴇʀ.

<b>-t thumbnail url:</b> Cᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ғᴏʀ ᴇᴀᴄʜ ʟᴇᴇxʜ.(ʀᴀᴡ ᴏʀ ᴛɢ ɪᴍᴀɢᴇ ᴜʀʟ)

<b>-ss value:</b> Gᴇɴᴇʀᴀᴛᴇ ꜱꜱ ғᴏʀ ʟᴇᴇᴄʜ ᴠɪᴅᴇᴏ, ᴍᴀx 𝟷𝟶 ғᴏʀ ᴇᴀᴄʜ ʟᴇᴀᴄʜ.

<b>-z or -z password:</b> Zɪᴘ ᴛʜᴇ ғɪʟᴇ ᴏʀ ғᴏʟᴅᴇʀ ᴡɪᴛʜ ᴏʀ ᴡɪᴛʜᴏᴜᴛ ᴘᴀꜱꜱᴡᴏʀᴅ.

<b>-e or -e password:</b> Exᴛʀᴀᴄᴛ ᴛʜᴇ ғɪʟᴇ ᴏʀ ғᴏʟᴅᴇʀ ᴡɪᴛʜ ᴏʀ ᴡɪᴛʜᴏᴜᴛ ᴘᴀꜱꜱᴡᴏʀᴅ.

<b>-up upload destination:</b> Uᴘʟᴏᴀᴅ ᴛʜᴇ ғɪʟᴇ ᴏʀ ғᴏʟᴅᴇʀ ᴛᴏ ᴀ ꜱᴘᴇᴄɪғɪᴄ ᴅᴇꜱᴛɪɴᴀᴛɪᴏɴ.

<b>-id drive_folder_link</b> or <b> -ɪᴅ ᴅʀɪᴠᴇ_ɪᴅ -ɪɴᴅᴇx ʜᴛᴛᴘꜱ://ᴀɴʏᴛʜɪɴɢ.ɪɴ/𝟶:: Uᴘʟᴏᴀᴅ ᴛᴏ ᴀ ᴄᴜꜱᴛᴏᴍ Gᴏᴏɢʟᴇ Dʀɪᴠᴇ ғᴏʟᴅᴇʀ ᴏʀ ID.

<b>-u username -p password:</b> Pʀᴏᴠɪᴅᴇ ᴀᴜᴛʜᴏʀɪᴢᴀᴛɪᴏɴ ғᴏʀ ᴀ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ.

<b>-s:</b> Sᴇʟᴇᴄᴛ ᴀ ᴛᴏʀʀᴇɴᴛ ғɪʟᴇ.

<b>-h Direct link custom headers:</b> -h
<code>/cmd</code> link -h Key: value Key1: value1.

<b>-d ratio:seed_time:</b> Sᴇᴛ ᴛʜᴇ ꜱᴇᴇᴅɪɴɢ ʀᴀᴛɪᴏ ᴀɴᴅ ᴛɪᴍᴇ ғᴏʀ ᴀ ᴛᴏʀʀᴇɴᴛ.

<b>-i number of links/files:</b> Pʀᴏᴄᴇꜱꜱ ᴍᴜʟᴛɪᴘʟᴇ ʟɪɴᴋꜱ ᴏʀ ғɪʟᴇꜱ.

<b>-m folder name:</b> Pʀᴏᴄᴇꜱꜱ ᴍᴜʟᴛɪᴘʟᴇ ʟɪɴᴋꜱ ᴏʀ ғɪʟᴇꜱ ᴡɪᴛʜɪɴ ᴛʜᴇ ꜱᴀᴍᴇ ᴜᴘʟᴏᴀᴅ ᴅɪʀᴇᴄᴛᴏʀʏ.

<b>-b:</b> Pᴇʀғᴏʀᴍ ʙᴜʟᴋ ᴅᴏᴡɴʟᴏᴀᴅ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇꜱꜱᴀɢᴇ ᴏʀ ғɪʟᴇ ᴡɪᴛʜ ᴍᴜʟᴛɪᴘʟᴇ ʟɪɴᴋꜱ ꜱᴇᴘᴀʀᴀᴛᴇᴅ ᴡɪᴛʜ ɴᴇᴡ ʟɪɴᴇ.

<b>-j:</b> Jᴏɪɴ ꜱᴘʟɪᴛ ғɪʟᴇꜱ ᴛᴏɢᴇᴛʜᴇʀ ʙᴇғᴏʀᴇ ᴇxᴛʀᴀᴄᴛɪɴɢ ᴏʀ ᴢɪᴘᴘɪɴɢ.

<b>-rcf:</b> Sᴇᴛ Rᴄʟᴏɴᴇ ғʟᴀɢꜱ ғᴏʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ.

<b>main:dump/ubuntu.iso</b> or <b>rcl:</b> Tʀᴇᴀᴛ ᴀ ᴘᴀᴛʜ ᴀꜱ ᴀɴ ʀᴄʟᴏɴᴇ ᴅᴏᴡɴʟᴏᴀᴅ."""

RSS_HELP_MESSAGE = """
Use this format to add feed URL:
Title1 link (required)
Title2 link -c cmd -inf xx -exf xx
Title3 link -c cmd -d ratio:time -z password

-c command + any arg
-inf: For included words filter.
-exf: For excluded words filter.

Example: Title <code>https://www.rss-url.com</code> inf: 1080 or 720 or 144p|mkv or mp4|hevc exf: flv or web|xxx opt: up: mrcc:remote:path/subdir rcf: --buffer-size:8M|key|key:value
This filter will parse links that have titles containing "(1080 or 720 or 144p) and (mkv or mp4) and hevc" and don't contain (flv or web) and xxx words. You can add whatever you want.

Another example: inf: 1080 or 720p|.web. or .webrip.|hevc or x264
This will parse titles that contain (1080 or 720p) and (.web. or .webrip.) and (hevc or x264). 
Note: I added spaces before and after "1080" to avoid wrong matching. If there is a number like "10805695" in the title, it won't match "1080" without spaces after it.

<b>Filter Notes:</b>
1. | means "and."
2. Add "or" between similar keys. For example, you can add it between qualities or between extensions. Avoid filters like "f: 1080|mp4 or 720|web" because this will parse "1080" and (mp4 or 720) and web, instead of (1080 and mp4) or (720 and web).
3. You can add "or" and "|" as much as you want.
4. Check the title for static special characters before or after the qualities, extensions, or other elements, and use them in the filter to avoid wrong matches.

<b>Timeout:</b> 60 sec.

<b>Please apply the same formatting to this message:</b>
"""

CLONE_HELP_MESSAGE = """
Send Gdrive link or rclone path along with command or by replying to the link/rc_path by command.

<b>Multi links only by replying to first gdlink or rclone_path:</b>
<code>/{cmd}</code> -i 10 (number of links/pathies)

<b>Gdrive:</b>
<code>/{cmd}</code> gdrivelink

<b>Upload Custom Drive:</b> link -id -index
-id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://anything.in/0:</code>
drive_id must be a folder ID, and index must be a URL, otherwise it will not accept.

<b>Rclone:</b>
<code>/{cmd}</code> (rcl or rclone_path) -up (rcl or rclone_path) -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue

Note: If -up is not specified, the rclone destination will be the RCLONE_PATH from config.env.
"""

PASSWORD_ERROR_MESSAGE = """
<b>This link requires a password!</b>
- Insert sign <b>::</b> after the link and write the password after the sign.
<b>Example:</b> {}::love you
Note: No spaces between the signs <b>::</b>
For the password, you can use a space!
"""
