import cloudinary
import cloudinary.uploader

# upload product image


def upload_product_image_cloudinary(img, public_name):  # public_name is product id
    upload_results = cloudinary.uploader.upload(
        img,
        public_id=public_name,
        folder="commerce_hub",
        overwrite=True,
        invalidate=True,
        resource_type="auto",
    )
    originalUrl = upload_results["secure_url"]

    thumbUrl = originalUrl.replace("/upload/", "/upload/c_thumb,w_300/")
    return {
        "msg": "image uploaded successfull",
        "uri": upload_results["secure_url"],
        "thumb_uri" : thumbUrl,
        "img_height": upload_results["height"],
        "img_width": upload_results["width"],
        "public_id": upload_results["public_id"],
        "folder": "commerce_hub",
    }


# delete product images


def destroy_product_image(img_id, folder="commerce_hub"):
    cloudinary.uploader.destroy(f"{folder}/{img_id}", invalidate=True)
    return {"msg": "image deleted successfullly"}
