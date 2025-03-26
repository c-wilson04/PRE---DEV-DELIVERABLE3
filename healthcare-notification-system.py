import datetime
from typing import List, Optional

class Notification:
    def __init__(self, notification_id: int, title: str, content: str, timestamp: datetime.datetime):
        self.notification_id = notification_id
        self.title = title
        self.content = content
        self.timestamp = timestamp
        self.is_read = False

class NotificationCenter:
    def __init__(self):
        self._notifications = []
        self._next_id = 1

    def add_notification(self, title: str, content: str) -> Notification:
        """
        Create and add a new notification to the system.
        
        Args:
            title (str): The title of the notification
            content (str): The detailed content of the notification
        
        Returns:
            Notification: The newly created notification
        """
        new_notification = Notification(
            notification_id=self._next_id,
            title=title,
            content=content,
            timestamp=datetime.datetime.now()
        )
        self._notifications.append(new_notification)
        self._next_id += 1
        return new_notification

    def get_unread_notifications(self) -> List[Notification]:
        """
        Retrieve all unread notifications.
        
        Returns:
            List[Notification]: List of unread notifications
        """
        return [notification for notification in self._notifications if not notification.is_read]

    def get_notification_by_id(self, notification_id: int) -> Optional[Notification]:
        """
        Retrieve a specific notification by its ID.
        
        Args:
            notification_id (int): The ID of the notification to retrieve
        
        Returns:
            Optional[Notification]: The notification if found, None otherwise
        """
        for notification in self._notifications:
            if notification.notification_id == notification_id:
                return notification
        return None

class HealthcareProviderSystem:
    def __init__(self):
        self.notification_center = NotificationCenter()
        self.current_user = None

    def login(self, username: str, password: str) -> bool:
        """
        Simulate user login process.
        
        Args:
            username (str): User's username
            password (str): User's password
        
        Returns:
            bool: True if login is successful, False otherwise
        """
        # In a real system, this would involve authentication
        if username and password:
            self.current_user = username
            print(f"User {username} logged in successfully.")
            return True
        return False

    def check_notifications(self) -> List[Notification]:
        """
        Check for new unread notifications.
        
        Returns:
            List[Notification]: List of unread notifications
        """
        if not self.current_user:
            print("Please log in first.")
            return []
        
        unread_notifications = self.notification_center.get_unread_notifications()
        print(f"Found {len(unread_notifications)} unread notifications.")
        return unread_notifications

    def view_notification(self, notification_id: int) -> Optional[Notification]:
        """
        View details of a specific notification and mark it as read.
        
        Args:
            notification_id (int): ID of the notification to view
        
        Returns:
            Optional[Notification]: The viewed notification, or None if not found
        """
        if not self.current_user:
            print("Please log in first.")
            return None
        
        notification = self.notification_center.get_notification_by_id(notification_id)
        
        if notification:
            print(f"Viewing Notification {notification_id}:")
            print(f"Title: {notification.title}")
            print(f"Content: {notification.content}")
            print(f"Timestamp: {notification.timestamp}")
            
            notification.is_read = True
            print("Notification marked as read.")
            
            return notification
        
        print(f"No notification found with ID {notification_id}")
        return None

# Example usage
def main():
    # Create healthcare provider system
    system = HealthcareProviderSystem()

    # Simulate login
    system.login("dr.smith", "secure_password")

    # Add some sample notifications
    system.notification_center.add_notification(
        "Patient Follow-up", 
        "Patient John Doe requires a follow-up consultation for recent test results."
    )
    system.notification_center.add_notification(
        "Urgent: Medication Update", 
        "Immediate review needed for patient medications due to potential interactions."
    )

    # Check notifications
    unread_notifications = system.check_notifications()

    # View first notification if available
    if unread_notifications:
        system.view_notification(unread_notifications[0].notification_id)

if __name__ == "__main__":
    main()
