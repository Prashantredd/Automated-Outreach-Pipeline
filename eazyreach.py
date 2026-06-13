class EazyreachService:
    def resolve_email(self, linkedin_url):
        if 'johndoe' in linkedin_url:
            return 'john.doe@example.com'
        if 'janesmith' in linkedin_url:
            return 'jane.smith@example.com'
        return None  