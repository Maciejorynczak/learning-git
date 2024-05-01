shopping_list = ["marchew", "seler", "rukola","chleb", "bułki", "pączek"]

shopping_dict = {
    "warzywniak": ["marchew", "seler", "rukola"],
    "piekarnia": ["chleb", "bułki", "pączek" ]
} 



for shop in shopping_dict:
    product = [product.capitalize() for product in shopping_dict[shop]]
    print(f"Idę do {shop.capitalize()} ,i kupuję tu następujące rzeczy: {product}.")
product_sum = sum(len(products) for products in shopping_dict.values())
print(f"W sumie kupuję {product_sum} produktów. ")