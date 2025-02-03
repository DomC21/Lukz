"""Feedback service for storing and managing user feedback"""
from typing import Dict
import json
import os
from datetime import datetime
from pathlib import Path

FEEDBACK_DIR = Path("data/feedback")

def save_feedback(feedback: Dict) -> bool:
    """Save feedback to a JSON file"""
    try:
        # Create feedback directory if it doesn't exist
        FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = FEEDBACK_DIR / f"feedback_{timestamp}.json"
        
        # Add metadata
        feedback_data = {
            "timestamp": datetime.now().isoformat(),
            "message": feedback.get("message", ""),
            "status": "new"
        }
        
        # Write to file
        with open(filename, "w") as f:
            json.dump(feedback_data, f, indent=2)
            
        return True
    except Exception as e:
        print(f"Error saving feedback: {str(e)}")
        return False
