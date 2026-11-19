from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.common.integration_type import IntegrationType

tx = Transaction(WebpayOptions(
    IntegrationCommerceCodes.WEBPAY_PLUS,
    IntegrationApiKeys.WEBPAY,
    IntegrationType.TEST
))

def generar_link_de_pago(buy_order: str, session_id: str, amount: float, return_url: str):
    return tx.create(buy_order, session_id, amount, return_url)

def confirmar_pago(token_ws: str):
    return tx.commit(token_ws)