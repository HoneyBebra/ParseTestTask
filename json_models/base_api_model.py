from pydantic import BaseModel


class SkuList(BaseModel):
    article: str | None
    skuId: str | None
    unitOfMeasure: str | None
    unitOfMeasureText: str | None
    merchant: str | None
    quantity: int | None


class Products(BaseModel):
    article: str | None
    repositoryId: str | None
    instalmentInfo: str | None
    defaultCategoryId: str | None
    fastDelivery: str | None
    brandName: str | None
    displayName: str | None
    largeImageUrl: str | None
    minSkuId: str | None
    minSkuName: str | None
    sefName: str | None
    relevanceCoefs: str | None
    franchise: str | None
    countReview: int | None
    numberOfSkuAvailable: int | None
    numberOfSkuInStock: int | None
    quantityInCart: int | None
    discountPercent: int | None
    discountDescription: str | None
    instalmentPayment: float | None
    instalmentPaymentAsString: str | None
    rating: float | None
    discountedPrice: float | None
    discountedPriceAsString: str | None
    priceWithoutCoupons: float | None
    priceWithoutCouponsAsString: str | None
    rawPrice: float | None
    rawPriceAsString: str | None
    minSkuPrice: float | None
    minSkuPriceAsString: str | None
    adultsOnly: bool | None
    isInWishList: bool | None
    isOnePriceForAllSkus: bool | None
    isOutOfStock: bool | None
    noLongerAvailable: bool | None
    showVolumes: bool | None
    skuList: list[SkuList] | None
    analyticsCategory: list | None
    color: list | None
    media: list | None
    appliedMarkers: list | None


class SortOptions(BaseModel):
    label: str | None
    value: str | None
    selected: bool | None


class BaseApiModel(BaseModel):
    """ All data """
    adultsOnly: bool | None
    products: list[Products] | None
    lastRecNum: int | None
    totalNumRecs: int | None
    totalNumSkus: int | None
    chanelProductsCount: int | None
    chanelRedirectEnabled: bool | None
    sortOptions: list[SortOptions] | None
