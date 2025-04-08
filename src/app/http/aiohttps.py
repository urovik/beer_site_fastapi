from aiohttp import ClientSession

from async_lru import alru_cache

@alru_cache
async def get_info_currency(amount:int):
    async with ClientSession() as session:
        url =  "https://api.apilayer.com/currency_data/convert?"
        params = {"to": "RUB",
                 "from" : "USD",
                 "amount" : amount, 
                 "apikey" : "RERvVKFk4b6VZJCDzJXRwWb2Ag2xsYnD"} 

        async with session.get(url=url,params=params) as response:
            try:
                result = await response.json()
                sums = result['result']
                return {"sum" : int(sums),"value" : "RUB"}
            except KeyError:
                return {'message':"Недопустимое число"}

            