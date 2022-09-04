import telebot
from telebot import types
from con.classes.SQL.StartingPostgres import *
from sqlalchemy import or_
import os

TOKEN = os.environ['TOKEN']

APP_URL = f"https://lokichangebot.herokuapp.com/{TOKEN}"

limit_time_send_photo = Sessions.query(ChangeInformation.limit_time_send_photo).filter(
    ChangeInformation.id == 1)[0][0]  # minutes

PATH = os.path.dirname(__file__)[:-17]

commission = Sessions.query(ChangeInformation.commission).filter(
    ChangeInformation.id == 1)[0][0]  # %

owner_id = Sessions.query(ChangeInformation.owner_id).filter(ChangeInformation.id == 1)[0][0]

arm_price = Sessions.query(ChangeInformation.amd_price).filter(ChangeInformation.id == 1)[0][0]

min_limits_amount_exchange = {
    "AMD": float(
        Sessions.query(ChangeInformation.min_limits_amount_exchange_amd).filter(ChangeInformation.id == 1)[0][0]),
    "USD": float(
        Sessions.query(ChangeInformation.min_limits_amount_exchange_usd).filter(ChangeInformation.id == 1)[0][0]),
    "BTC": float(
        Sessions.query(ChangeInformation.min_limits_amount_exchange_btc).filter(ChangeInformation.id == 1)[0][0]),
    "DASH": float(
        Sessions.query(ChangeInformation.min_limits_amount_exchange_dash).filter(ChangeInformation.id == 1)[0][0]),
    "XRP": float(
        Sessions.query(ChangeInformation.min_limits_amount_exchange_xrp).filter(ChangeInformation.id == 1)[0][0]),
    "USDT": float(
        Sessions.query(ChangeInformation.min_limits_amount_exchange_ltc).filter(ChangeInformation.id == 1)[0][0]),
}

max_limits_amount_exchange = {
    "AMD": float(
        Sessions.query(ChangeInformation.max_limits_amount_exchange_amd).filter(ChangeInformation.id == 1)[0][0]),
    "USD": float(
        Sessions.query(ChangeInformation.max_limits_amount_exchange_usd).filter(ChangeInformation.id == 1)[0][0]),
    "BTC": float(
        Sessions.query(ChangeInformation.max_limits_amount_exchange_btc).filter(ChangeInformation.id == 1)[0][0]),
    "DASH": float(
        Sessions.query(ChangeInformation.max_limits_amount_exchange_dash).filter(ChangeInformation.id == 1)[0][0]),
    "XRP": float(
        Sessions.query(ChangeInformation.max_limits_amount_exchange_xrp).filter(ChangeInformation.id == 1)[0][0]),
    "USDT": float(
        Sessions.query(ChangeInformation.max_limits_amount_exchange_ltc).filter(ChangeInformation.id == 1)[0][0]),
}

wallets = {
    "idram": Sessions.query(ChangeInformation.owner_walet_idram).filter(ChangeInformation.id == 1)[0][0],
    "telcell": Sessions.query(ChangeInformation.owner_walet_telcell).filter(ChangeInformation.id == 1)[0][0],
    "easypay": Sessions.query(ChangeInformation.owner_walet_easypay).filter(ChangeInformation.id == 1)[0][0],
}
# 1,20,5,400,1357108258,3000,7,0.00032,0.139,20,0.121,500000,1000,0.1,20,2856,17.421,099-99-99-99,099-99-99-99,099-99-99-99,3J6GpcD4ImA2ZyEMvtKLCYcoRs,3J6GpcD4ImA2ZyEMvtKLCYcoRs,3J6GpcD4ImA2ZyEMvtKLCYcoRs,3J6GpcD4ImA2ZyEMvtKLCYcoRs
