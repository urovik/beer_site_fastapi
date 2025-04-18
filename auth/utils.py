from datetime import datetime, timedelta


import jwt 
import bcrypt

from config.pydantics_settings import jwt_config

SECRET_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAlfCeAU4AKKHu4aLHIm+Z0k1E/JIj0XYM0annT/rV5PH8CUPv
KWCCdtS+CStqfGpVUNkKCXYZotkG07I7ufOlKIU+bLetCu0zcYFHTa8r6fcdQCYL
utOsqtHZd482b8Mrkc6XYbf7erKHLJGwzs0VDIfPnM1h8gr/PHICnintguIWUrja
P/IQWEb13ARYV19A4Y4YNwA6xLyEQcSpBszfDd8B7nsV5chMhydiFPcZDHdp6z2l
q9fFTxJNzk4sKsCU1iD4Mo9DnJ9K/ftrHRWuG5RwJkvfBFJdgF1Fyb0sH8XpG+2Y
e285ySxAdJeAkczGuaEvXOqRLhjqHLkBPOB8ZwIDAQABAoIBAQCEykGVFDhtw+Qk
7p1/sOjA6G/VY7PXGL6HnPpfyd1O0sSMjB6uPWutxAG9azb2ktGWNXF/KZnQsHYs
XCgrKk210jOT4yOcjrBFsOGuOhohLho4qrkur7K24fy/txTV7DqU+ir1fxR3+M5g
OXMl41jl7Q2AaCB7VSPwq2QIIUfY5ffm4sKv02ib5MJCibS1bXuIGxSQ7YwkOMrE
DjCUmRNkUUm4iy+oyn+E//1WZhXm0Hhta8bZ2585p6ShujpQIZyr9N6GVW38BTUL
1/+LXNCEcR6aelIlFRzpn7jw0rVFXMLGKiJuCFtKr3mN29Tilh7SeVmbhRxDT/oR
hxO+DcpJAoGBANVdFh7foRpsqDjziajjkH+3SV+yuyhiYeqYW9/kmVj8P+0/SsXC
Otylgpgp+FCgvpTrwv++O5MfxKxTkmU8ztdsrZ1m5UjZka+8JL1H2AoNFlpdbhqq
F/VO5+dXyubgv3//l3ukPvLNMRMyUlQhHtF4J9QD/Ne4IVfIXB8G2+yrAoGBALPn
AKZ8FL6B+5c9WX+UDH/xHdr36s6aGckRgF8EojSKSSE6ofQEgmwWBuy+MJLcxlhj
Vx1TpiaLNYVQzUUGUWmntHRAyidtRgOpfB8rB/+trgdoWQnIlQUaqCoH2D9BlUWR
3jgUhj1q2DHV7voWBuJe/DC5IrBVUFSRrMuI/3c1AoGAfCMGpbvSzb7+OPRo2Vxd
TBFlnUot3hcvhQBUI/Wqyr0orG4woNKa0JlzW/i/QpnjiF2LPKR/oN/Q27pb6I7y
gR/3+yZMrI/5VVePwJi2N1LZ+IV3dAgWnGDmSBEqOh31DRG2Hve2sCl2LgcPI2eJ
uLHB6nbPeurka2BlSKADALUCgYEAiAihAULKHNQE/nOxfTrhyMz2GmFk+BymatgF
DdRfIwN+ENZZKD9Qr5JoYhPefu7aPHPBp7dc58BUFB7pWMxSO2ZIma90LSP/0T0T
Ui4juj4GXiuVSESYCmgByOZtqkdZLGYEdrtuVnq4R9bRAeIuCnZwlBcqF9QrDgep
da5+HhECgYBjtN5MeU+k2H7gApLDIzOXjydz2Fa59lvEGeQFPl0TI9DXZcNZF/LO
q8mcD2UomrpLxHN+3nH37MVXXIL1MQA7pJszvj35XmXdrZo/UbMElZXaCXsmdKuR
aKi7R3O0RHhqzNstsHUuXEJX8aj4Ilmb//BTxlGso1+wz9GupuJtmA==
-----END RSA PRIVATE KEY-----"""
PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlfCeAU4AKKHu4aLHIm+Z
0k1E/JIj0XYM0annT/rV5PH8CUPvKWCCdtS+CStqfGpVUNkKCXYZotkG07I7ufOl
KIU+bLetCu0zcYFHTa8r6fcdQCYLutOsqtHZd482b8Mrkc6XYbf7erKHLJGwzs0V
DIfPnM1h8gr/PHICnintguIWUrjaP/IQWEb13ARYV19A4Y4YNwA6xLyEQcSpBszf
Dd8B7nsV5chMhydiFPcZDHdp6z2lq9fFTxJNzk4sKsCU1iD4Mo9DnJ9K/ftrHRWu
G5RwJkvfBFJdgF1Fyb0sH8XpG+2Ye285ySxAdJeAkczGuaEvXOqRLhjqHLkBPOB8
ZwIDAQAB
-----END PUBLIC KEY-----"""


def encode_jwt(
        payload: dict,
        private_key: str = SECRET_KEY,
        algorithm: str = jwt_config.algorithm,
        expire_minutes: int = jwt_config.expire_minutes
    ):
    to_encode = payload.copy()
    now = datetime.utcnow()
    expire = now + timedelta(minutes=int(expire_minutes))
    to_encode.update({'exp' : expire})
    encoded = jwt.encode(to_encode,private_key,algorithm=algorithm)
    return encoded

def decode_jwt(
    token: str | bytes,
    public_key: str = PUBLIC_KEY,
    algorithm: str = jwt_config.algorithm
):
    decoded = jwt.decode(token,public_key,algorithms=[algorithm])
    return decoded


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd_pass: bytes = password.encode()
    return bcrypt.hashpw(pwd_pass,salt)

def validate_password(
        password: str,
        hash_password: bytes
) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        hash_password
)