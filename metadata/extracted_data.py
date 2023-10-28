import UIKit
import ImageIO

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        url_strings = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg"
        ]

        # Convert the URL strings to actual URL objects
        url_objects = [urllib.parse.urlparse(url) for url in url_strings]
        # Now, url_objects is a list of URL objects
        
        let photoURLs: [URL] = getPhotoURLs() // Replace with your array of photo URLs

        for imageURL in photoURLs {
            extractMetadata(from: imageURL)
        }
    }

    func extractMetadata(from imageURL: URL) {
        if let imageSource = CGImageSourceCreateWithURL(imageURL as CFURL, nil) {
            if let imageProperties = CGImageSourceCopyPropertiesAtIndex(imageSource, 0, nil) as? [String: Any] {
                print("Metadata for \(imageURL.lastPathComponent):")
                print(imageProperties)
                
                // To extract specific metadata, for example, the EXIF data:
                if let exifData = imageProperties[kCGImagePropertyExifDictionary as String] as? [String: Any] {
                    print("EXIF data for \(imageURL.lastPathComponent):")
                    print(exifData)
                }
            }
        }
    }
    
    func getPhotoURLs() -> [URL] {
        // Replace this with your logic to obtain URLs of HEIF/HEVC photos
        // For example, you can use a file picker or load them from a specific directory.
        // Ensure that you populate and return an array of valid photo URLs.
        
        // Example: Load photos from the app's bundle
        if let photo1URL = Bundle.main.url(forResource: "photo1", withExtension: "heic"),
           let photo2URL = Bundle.main.url(forResource: "photo2", withExtension: "heic") {
            return [photo1URL, photo2URL]
        }
        
        return []
    }
}
