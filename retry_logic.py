import asyncio
import httpx
from httpx import RequestError, HTTPStatusError
from app.utils.helpers import LoggerHelper

logger = LoggerHelper.get_logger("retry_logic")

async def make_request_with_retry(
    url: str,
    method: str = "POST",
    retries: int = 3,
    timeout: httpx.Timeout = httpx.Timeout(120.0, connect=10.0),
    headers: dict = None,
    files: dict = None,
    data: dict = None,
) -> dict:
    """
    Makes an HTTP request with retry logic.

    :param url: Target URL for the request.
    :param method: HTTP method to use (default: POST).
    :param retries: Number of retry attempts (default: 3).
    :param timeout: Timeout configuration for the request.
    :param headers: Optional HTTP headers.
    :param files: Optional files for upload.
    :param data: Optional data for the request.
    :return: A dictionary with the response status code and JSON body.
    """
    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(retries):
            try:
                logger.info(f"Attempt {attempt + 1} of {retries} for {url}")
                
                response = await client.request(method, url, headers=headers, files=files, data=data)
                response.raise_for_status()  # Raise for 4xx/5xx HTTP errors
                
                raw_response = response.json()
                logger.info(f"Request successful: {response.status_code}")
                
                return {
                    "status_code": response.status_code,
                    "json": raw_response
                }
            except HTTPStatusError as exc:
                if exc.response.status_code in {429, 503} and attempt < retries - 1:
                    logger.warning(f"Transient error {exc.response.status_code}: Retrying in 2 seconds...")
                    await asyncio.sleep(2)  # Wait before retrying
                else:
                    logger.error(f"HTTP error: {exc.response.status_code} - {exc.response.text}")
                    return {
                        "status_code": exc.response.status_code,
                        "json": {"error": exc.response.text}
                    }
            except RequestError as exc:
                logger.error(f"Request error: {exc}")
                if attempt < retries - 1:
                    logger.info(f"Retrying in 2 seconds... (attempt {attempt + 1} of {retries})")
                    await asyncio.sleep(2)
                else:
                    logger.critical("Max retries exceeded.")
                    return {
                        "status_code": 500,
                        "json": {"error": "Max retries exceeded"}
                    }
            except Exception as e:
                logger.exception(f"Unexpected error: {str(e)}")
                return {
                    "status_code": 500,
                    "json": {"error": str(e)}
                }



#########################################################
# And you can use the method lie this 

# @app.post("/proxy-request")
# async def proxy_request():
#     url = "https://example.com/api"  # Replace with your target API
#     headers = {"Authorization": "Bearer YOUR_TOKEN"}  # Add headers if needed
#     data = {"key": "value"}  # Add data if needed

#     try:
#         result = await make_request_with_retry(url, headers=headers, data=data)
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Request failed: {str(e)}")