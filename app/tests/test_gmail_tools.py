import unittest
from unittest.mock import patch, MagicMock
import datetime
from app.tools.gmail_manager import get_important_emails_summary, identify_space_optimization_targets, get_email_metrics

class TestGmailTools(unittest.TestCase):

    @patch('app.tools.gmail_manager.get_gmail_service')
    @patch('app.tools.gmail_manager.init_gmail_db')
    def test_get_important_emails_summary(self, mock_init_db, mock_get_service):
        mock_service = MagicMock()
        mock_get_service.return_value = mock_service

        mock_service.users().messages().list().execute.return_value = {
            'messages': [{'id': '123'}]
        }

        mock_service.users().messages().get().execute.return_value = {
            'id': '123',
            'snippet': 'Important message snippet',
            'payload': {
                'headers': [
                    {'name': 'Subject', 'value': 'Important Subject'},
                    {'name': 'From', 'value': 'boss@work.com'}
                ]
            }
        }

        result = get_important_emails_summary.invoke({})
        self.assertIn("boss@work.com", result)
        self.assertIn("Important Subject", result)
        self.assertIn("Important message snippet", result)

    @patch('app.tools.gmail_manager.get_gmail_service')
    @patch('app.tools.gmail_manager.init_gmail_db')
    def test_identify_space_optimization_targets(self, mock_init_db, mock_get_service):
        mock_service = MagicMock()
        mock_get_service.return_value = mock_service

        # Mocking large messages
        mock_service.users().messages().list().execute.side_effect = [
            {'messages': [{'id': 'large1'}]}, # for larger:10M
            {'messages': [{'id': 'old1'}]}    # for before:2years
        ]

        mock_service.users().messages().get().execute.return_value = {
            'id': 'large1',
            'sizeEstimate': 15 * 1024 * 1024
        }

        result = identify_space_optimization_targets.invoke({})
        self.assertIn("E-mails com anexos grandes (>10MB)", result)
        self.assertIn("large1", result)
        self.assertIn("E-mails com mais de 2 anos", result)

    @patch('app.tools.gmail_manager.get_gmail_service')
    def test_get_email_metrics(self, mock_get_service):
        mock_service = MagicMock()
        mock_get_service.return_value = mock_service

        mock_service.users().messages().list().execute.side_effect = [
            {'resultSizeEstimate': 5}, # important
            {'resultSizeEstimate': 10}, # large attachments
            {'resultSizeEstimate': 100} # old emails
        ]

        result = get_email_metrics.invoke({})
        self.assertEqual(result['important_last_7_days'], 5)
        self.assertEqual(result['large_attachments_count'], 10)
        self.assertEqual(result['old_emails_count'], 100)
        self.assertIn('last_updated', result)

if __name__ == '__main__':
    unittest.main()
