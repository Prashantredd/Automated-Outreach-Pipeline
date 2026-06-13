from services.ocean import OceanService
from services.prospeo import ProspeoService
from services.eazyreach import EazyreachService
def main():
    domain = input("Enter company domain: ")

    ocean = OceanService()
    prospeo=ProspeoService()
    easyreach=EazyreachService()

    companies = ocean.get_similar_companies(domain)
    contacts=[]
    print("\nSimilar Companies:")
    for company in companies:
        print(f"\nCompany:{company}")
        people =prospeo.get_decision_makers(company)
        for person in people:
            email=easyreach.resolve_email(person['linkedin_url'])
            print(f"Name :{person['name']} | " f"Title: {person['title']}) | "
            f"Linkedin: {person['linkedin_url']}")
            contacts.append({'comapny':company,'name':person['name'],'title':person['title'],'email':email})
    print("\nCONTACTS FOUND")  
    for contact in contacts: 
        print( f"{contact['name']} | " f"{contact['title']} | " f"{contact['email']}" ) 

if __name__ == "__main__":
    main()