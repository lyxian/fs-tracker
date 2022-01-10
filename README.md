# Manual Lazada Flash Sale

**Steps**

0. go to : https://pages.lazada.sg/wow/i/sg/LandingPage/flashsale-h5
1. run `web.js` commands in Chrome console
2. save all requests as HAR (try filter unwanted)
3. run `urls.py` to extract URLs
4. run `main.py` to compile sale items

## Web.js

function sleep(ms) {
return new Promise(resolve => setTimeout(resolve, ms));
}

document.querySelectorAll('a.button').forEach(button => {
if (button.dataset.campIndex != '0') {button.remove()};
});

for (let i = 0; i < 40; i++) {
document.querySelector('a.button').click()
await sleep(3000);
}

## Dashboard

- show top 10 best selling products by:
  - sold ratio
  - item rating
  - item discount
  - category
- check difference in products
- classify products based on name

## ITEMS

- key props :
  - itemPrice
  - itemDiscount
  - itemDiscountPrice
  - itemCurrentStock
  - itemTotalStock
  - itemSoldRatio
  - itemTitle
  - itemUrl > fs_min_price_l30d
  - itemImg
  - itemSoldCnt
  - itemHaveStock
  - almostSoldOut
  - isHot
  - bizCategory?
  - shopName
  - itemReviews
  - itemRatingScore
  - trackInfo > fs_min_price_l30d
  - lowestPrice
- bizCategory :
  { "id": 1, "text": "Electronics & Appliances" },
  { "id": 2, "text": "Health & Beauty" },
  { "id": 3, "text": "Home & Living" },
  { "id": 4, "text": "Baby & Toys" },
  { "id": 5, "text": "Fashion & Sports" },
  { "id": 6, "text": "Groceries & Pets" },
  { "id": 7, "text": "Lifestyle" }

## NOTES

- sort items / urls
- https://www.lazada.sg/products/i<id/itemId>-s<skuId>.html
  - eg. https://www.lazada.sg/products/i1908965381-s10201991239.html
