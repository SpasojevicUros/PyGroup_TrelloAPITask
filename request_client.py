import requests
import logging

logger = logging.getLogger(__name__)

class RequestClient:
    
    def __init__(self, base_url, api_key = None, api_token = None):
        self.base_url = base_url
        self.api_key = api_key
        self.api_token = api_token
        self.headers = {
            'Accept': 'application/json'
        }
        self.default_params = {}
        
        if api_key and api_token:
            self.default_params.update({
                'key': api_key,
                'token': api_token
            })
            
        logger.info("RequestHandler initialized")
            
    def _prepare_params(self, new_params):
        params = self.default_params.copy()
        params.update(new_params)
        return params
            
    def get(self, endpoint, new_params = {}):
        
        params = self._prepare_params(new_params)
        
        try:
            response = requests.get(self.base_url + endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            logger.info(f"GET request to {endpoint} successful")
            return response.json()
        except requests.exceptions.HTTPError as httpError:
            logger.error(f"HTTP error occurred: {httpError}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
    
    def post(self, endpoint, new_params = {}, data = {}):
        
        params = self._prepare_params(new_params)
        
        try:
            response = requests.post(self.base_url + endpoint, headers=self.headers, params=params, data=data)
            response.raise_for_status()
            logger.info(f"POST request to {endpoint} successful")
            return response.json()
        except requests.exceptions.HTTPError as httpError:
            logger.error(f"HTTP error occurred: {httpError}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            
    def put(self, endpoint, new_params = {}, data = {}):
            
        params = self._prepare_params(new_params)
        
        try:
            response = requests.put(self.base_url + endpoint, headers=self.headers, params=params, data=data)
            response.raise_for_status()
            logger.info(f"PUT request to {endpoint} successful")
            return response.json()
        except requests.exceptions.HTTPError as httpError:
            logger.error(f"HTTP error occurred: {httpError}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            
    def delete(self, endpoint, new_params = {}):
        
        params = self._prepare_params(new_params)
        
        try:
            response = requests.delete(self.base_url + endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            logger.info(f"DELETE request to {endpoint} successful")
            return response.json()
        except requests.exceptions.HTTPError as httpError:
            logger.error(f"HTTP error occurred: {httpError}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
