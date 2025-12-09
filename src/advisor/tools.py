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
    try:
        return {
            "status": "success",
            # Static LinkedIn profile hosted in Github public project to avoid using LinkedIn MCP server or API
            "service_offerings": crawl_website("https://raw.githubusercontent.com/ahsan-ikram/ahsan-ikram/refs/heads/main/Static%20LinkedIn%20(Ahsan%20Ikram).html"),
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"The professional background of Ahsan Ikram are currently not available {e}",
        }
        
