class TorrentNotFoundException(Exception):
	"""An exception thrown when an operation is performed on a torrent object that 
	does not exist.
	""" 
	pass

class TransmissionClient(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def get_torrent(self, t_id):
		pass
	def get_torrents(self, t_ids):
		pass

	def add_torrent(self):
		pass
	def add_torrents(self):
		pass

	def delete_torrent(self, t_id):
		pass
	def delete_torrents(self, t_ids):
		pass
	
