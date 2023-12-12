from os import environ
import logging
import requests
import base64

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")

#Yhis is the ERC721 portal addrress for cartesi rollups
ERC721_PORTAL_ADDRESS = "0x237F8DD094C0e47f4236f12b4Fa01d6Dae89fb87".lower()

last_token_id = 0

def str2hex(string):
    """
    Encode a string as an hex string
    """
    return binary2hex(str2binary(string))

def hex2str(hexstr):
    """
    Decodes a hex string into a regular string
    """
    return hex2binary(hexstr).decode("utf-8")

def hex2binary(hexstr):
    """
    Decodes a hex string into a regular byte string
    """
    return bytes.fromhex(hexstr[2:])

def str2binary(string):
    """
    Encode a string as an binary string
    """
    return string.encode("utf-8")

def binary2hex(binary):
    """
    Encode a binary as an hex string
    """
    return "0x" + binary.hex()


def send_notice(notice):
    send_post("notice",notice)

def send_voucher(voucher):
    send_post("voucher",voucher)

def send_post(endpoint,json_data):
    response = requests.post(rollup_server + f"/{endpoint}", json=json_data)
    logger.info(f"/{endpoint}: Received response status {response.status_code} body {response.content}")


def handle_advance(data):
    logger.info(f"Received advance request data")
    logger.info(data)
    status = "accept"
    sender = data["metadata"]["msg_sender"].lower()
    try:
        payload = hex2str(data["payload"])
        if payload == "create":
            logger.info("Received 'create' command to mint NFT")
            mint_nft(sender)
        else:
            logger.info(f"Received non-create payload: {payload}")
    except Exception as e:
        status = "reject"
        msg = f"Error processing request: {e}"
        traceback.print_exc()
        logger.error(msg)
        send_report({"payload": str2hex(msg)})

    # Sending a notice back with the payload
    payload = str2hex(str(payload))
    notice = {"payload": payload}
    send_notice(notice)
    logger.info(f"Notice payload was {payload}")
    return status

def handle_inspect(data):
    logger.info(f"Received inspect request data {data}")
    return "accept"


def mint_nft(sender):
    global last_token_id

    last_token_id += 1
    token_id = last_token_id

    logger.info(f"Minting NFT for sender: {sender}")
    token_uri = "https://example.com/nft/metadata.json" #just a sample here.
    
    data = sender + str(token_id) + token_uri

    mint_payload = str2hex(data)
    voucher = {"destination": ERC721_PORTAL_ADDRESS, "payload": mint_payload}

    logger.info(f"Generated voucher for NFT minting: {voucher}")
    send_voucher(voucher)


handlers = {
    "advance_state": handle_advance,
    "inspect_state": handle_inspect,
}

finish = {"status": "accept"}

while True:
    logger.info("Sending finish")
    response = requests.post(rollup_server + "/finish", json=finish)
    logger.info(f"Received finish status {response.status_code}")
    if response.status_code == 202:
        logger.info("No pending rollup request, trying again")
    else:
        rollup_request = response.json()
        data = rollup_request["data"]
        handler = handlers[rollup_request["request_type"]]
        finish["status"] = handler(rollup_request["data"])
