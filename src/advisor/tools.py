from helper import crawl_website


def get_service_offerings() -> dict:
    try:
        return {
            "status": "success",
            "service_offerings": crawl_website("https://www.ahsanikram.com/"),
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"The service offerings of Ahsan Ikram are currently not available {e}",
        }

def get_professional_experience() -> dict:
    return {
            "status": "error",
            "error_message": f"The professional background is currently not available ",
        }
        
