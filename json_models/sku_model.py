from pydantic import BaseModel
from typing import Any


class Price(BaseModel):
    high: float | None
    low: float | None
    lowAsString: str | None
    highAsString: str | None


class TopSpecs(BaseModel):
    nameTooltip: str | None
    name: str | None
    value: str | None


class Media(BaseModel):
    type: str | None
    url: str | None


class Brand(BaseModel):
    corner: bool | None
    favorite: bool | None
    navigationState: str | None
    id: str | None
    imageUrl: str | None
    name: str | None


class Recipe(BaseModel):
    message: str | None
    isRecipe: bool | None
    isError: bool | None


class ReviewCountByRatingInfo(BaseModel):
    rating: int | None
    count: int | None


class NlpBonusInfo(BaseModel):
    premiumBonusAmount: int | None
    bonusAmount: int | None


class InstallmentsInfo(BaseModel):
    fractionValue: int | None
    fractionValueMessage: str | None
    fractionMessage: str | None


class SkuListPrice(BaseModel):
    listPriceAsString: str | None
    nlpBonusInfo: NlpBonusInfo | None
    installmentsInfo: InstallmentsInfo | None
    amountAsString: str | None
    amount: float | None
    listPrice: float | None
    discountPercent: int | None
    discountDescription: str | None
    priceWithMaxDCardAsString: str | None
    priceWithMaxDCard: float | None


class Image(BaseModel):
    url: str | None
    mimeType: str | None


class Shade(BaseModel):
    colors: list | None
    image: Image | None
    name: str | None


class SkuList(BaseModel):
    price: SkuListPrice | None
    quantityInCart: int | None
    id: str | None
    displayName: str | None
    media: list[Media] | None
    volume: str | None
    merchant: Any | None
    article: str | None
    unitOfMeasure: str | None
    shade: Shade | None
    canAddPostcard: bool | None
    appliedMarkers: list | None
    isAvailable: bool | None
    isEmblematic: bool | None
    isInStock: bool | None
    greatImageURL: str | None
    isInWishlist: bool | None


class SkuModel(BaseModel):
    """ All data """
    price: Price | None
    analyticsCategory: list[str] | None
    rating: float | None
    topSpecs: list[TopSpecs] | None
    displayName: str | None
    productId: str | None
    enableNlp: bool | None
    media: list[Media] | None
    sefPath: str | None
    brand: Brand | None
    recipe: Recipe | None
    countReview: int | None
    reviewCountByRatingInfo: list[ReviewCountByRatingInfo] | None
    productGroupList: list | None
    defaultCategoryName: str | None
    skuList: list[SkuList] | None
    isNoLongerAvailable: bool | None
    isAdultsOnly: bool | None
    isInWishList: bool | None
