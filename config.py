import os

class Config(object):
	API_HASH = os.getenv('API_HASH','1264d2d7d397c4635147ee25ab5808d1')
	BOT_TOKEN = os.getenv('BOT_TOKEN','5350577440:AAF0zQQ8Ka291A3mzhdWEgJ_vL-_TtC2y_M')
	API_ID = int(os.getenv('API_ID','3477714'))
	OWNER = int(os.environ.get('OWNER','589641907'))
	OWNER_USERNAME = os.getenv('OWNER_USERNAME','TrueShikari')
	PASSWORD = os.getenv('PASSWORD','12345678')
	DATABASE_URL=os.environ.get("DATABASE_URL","mongodb+srv://shikari:shikari@cluster0.srfww.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	FLAG = int(os.getenv('FLAG',1))		# Dont Change this(unfinished feature!!) or else bot will stop working
	LOGCHANNEL = os.getenv('LOGCHANNEL') or None # Add channel id with -100 /\or/\ channel user name without @
