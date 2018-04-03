from django.test import TestCase


class SendLoginEmailViewTest(TestCase):
    """Send Login Email View Test."""

    def test_redirects_to_home_page(self):
        """Test redirects to home page."""
        response = self.client.post('/accounts/send_login_email', data={
            'email': 'edith@example.com'
        })
        self.assertRedirects(response, '/')
