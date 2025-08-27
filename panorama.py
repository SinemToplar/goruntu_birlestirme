import image_stitching.read_images as read_images
import image_stitching.recursion as recursion
import sys
import cv2


def main(image_dir_list):
    """ Komut satırından verilen görüntü dizinlerini alır, panorama birleştirme işlemini çalıştırır ve sonucu /outputs/ klasörüne kaydeder."""

    print("PANORAMA")
    images_list, no_of_images = read_images.read(image_dir_list)
    
    # DEBUG SATIRLARI
    print(f"Resim sayısı: {no_of_images}")
    print(f"Resim dosyaları: {image_dir_list}")
    
    if no_of_images < 2:
        print("Hata: En az 2 resim gerekli!")
        return
        
    if len(images_list) == 0:
        print("Hata: Resimler okunamadı!")
        return
    
    print(f"İlk resmin boyutu: {images_list[0].shape if images_list[0] is not None else 'None'}")
    print(f"İkinci resmin boyutu: {images_list[1].shape if images_list[1] is not None else 'None'}")
    print(f"Üçüncü resmin boyutu: {images_list[2].shape if images_list[2] is not None else 'None'}")
    
    result, mapped_image = recursion.recurse(images_list, no_of_images)
    
    # Çıktı dosya isimleri listesi (aynı sırada)
    output_list = [
        "outputs/panorama_image.jpg",
        "outputs/mapped_image.jpg"
    ]
    
    cv2.imwrite(output_list[0], result)
    cv2.imwrite(output_list[1], mapped_image)

    print(f"Panoramik görüntü kaydedildi: {output_list[0]}")
    print(f"Mapped görüntü kaydedildi: {output_list[1]}")
    

if __name__ == "__main__":
    
    image_list = [
        "inputs/1.jpg",
        "inputs/2.jpg", 
        "inputs/3.jpg"
    ]
    
    print(f"Kullanılacak resimler: {image_list}")
    main(image_list)