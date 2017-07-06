import base64
import json
import requests
import torrent

class TorrentNotFoundException(Exception):
	"""An exception thrown when an operation is performed on a torrent object that 
	does not exist.
	""" 
	pass

class InvalidTransmissionQuery(Exception):
    """An exception thrown when a query is improperly structured when passed to the
    TransmissionClient
    """
    pass

class TransmissionClient(object):
        def _post_request(self, data):
            """Prepares the request to the Transmission client.

            Sets the authentication for the client, as well as the data to be requested.
            Resets the X-Transmission-Session-Id as needed.

            data (json) -- A json representation of the data to be transmitted/requested.

            Returns the response from the Transmission Daemon.
            """
            url = "http://{}:{}/transmission/rpc".format(self.host, self.port)
            # Post request
            response = requests.post(url, data=data, auth=(self.username, self.password), 
                    headers={ "X-Transmission-Session-Id": self.session_id })
            # Check if the session id needs to be renewed.
            if response.status_code == 409:
                self.session_id = response.headers["X-Transmission-Session-Id"]
                return requests.post(url, data=data, auth=(self.username, self.password),
                        headers={ "X-Transmission-Session-Id": self.session_id })
	    return response

        def __init__(self, host, port=9091, username="transmission", password="transmission"):
            """Initializes the client to communicate with the Transmission API over the network.
            
            username (string) -- The username used for authentication with the Transmission Daemon.
            password (string) -- The password used for authentication with the Transmission Daemon.
            host (string) -- The hostname where the Transmission Daemon is located.
            port (int) -- The port where the Transmisison Daemon is serving.
            session_id (string) -- The X-Transmission-Session-Id currently being used to protect against XSRF attacks.
            """
	    self.username = username
	    self.password = password
            self.host = host
            self.port = port
            self.session_id = ""

        # Action Requests 
        def start_torrents(self, t_ids=[]):
            data = {}
            if t_ids == []:
                data["arguments"] = {}
            else:
                data["ids"] = t_ids
            data["method"] = "torrent-start"
        
        def stop_torrent(self, t_id):
            data = {}
            if t_ids == []:
                data["arguments"] = {}
            else:
                data["arguments"] = { 
                        "ids": t_ids,
                }
            data["method"] = "torrent-stop"

	def get_torrents(self, t_ids=[], fields=["id", "name", "totalSize"]):
            """Returns the specified torrent file(s). If none are specified, returns all.

            t_ids ([]int) -- An array of torrent ids.
            fields ([]string) -- An array of strings indicating the desired attributes of a torrent file(s) to return. Must be of length greater than 1.
            """
            if len(fields) < 1:
                raise InvalidTransmissionQuery("invalid 'torrent-get' query")
            
            data = {}
            if t_ids == []:
                data["arguments"] = { "fields": fields }
            else:
                data["arguments"] = { 
                        "fields": fields,
                        "ids": t_ids,
                }
            data["method"] = "torrent-get"

            json_data = json.dumps(data)
            response = self._post_request(json_data)
            torrents = []
            json_resp = json.loads(response.text)
            for torr in json_resp["arguments"]["torrents"]:
                torrents.append(torrent.Torrent(data=torr))
            return torrents

	def add_torrents(self):
		pass

	def delete_torrents(self, t_ids, delete_local_data=False):
		pass
	
