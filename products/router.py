from fastapi import APIRouter,HTTPException,status


from .schemas import ProductSchema
from .service import ProductService

router = APIRouter(prefix = '/api/products',tags=["products"])


@router.get("/all")
async def get_all_products():
    return await ProductService.get_all_products_from_db()

@router.post("")
async def add_products(product: ProductSchema):
    existing_product = await ProductService.get_product_by_name(product.name)
    if existing_product:
        return HTTPException(
            status_code= status.HTTP_409_CONFLICT,
            detail="Такой продукт уже существует"
        )
    await ProductService.add_products_on_table(product.name,product.description,product.manafacture,product.type)
    return {"message":"продукт добавлен"}

@router.post("/types")
async def add_type(type: str):
    existing_type = await ProductService.get_type_from_db(type)
    if existing_type:
        return HTTPException(
            status_code= status.HTTP_409_CONFLICT,
            detail="Такой тип продукта уже существует"
        )
    await ProductService.add_type_product_on_table(type)
    return {"message":"Добавлен новый тип продукта"}

@router.get("/types/{type}")
async def get_type_product(type: str):
    return await ProductService.get_type_from_db(type)

@router.get("/types")
async def get_all_type_products():
    return await ProductService.get_all_type_products_from_db()
    