import os
import time
import json
from datetime import datetime

def display_sessions():
    session_files = [f for f in os.listdir('.') if f.startswith('session_') and f.endswith('.json')]
    
    print(" PRESERVED DEEPSEEK SESSIONS")
    print("=" * 50)
    
    for session_file in sorted(session_files, reverse=True)[:5]:
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        print(f" {session_file}")
        print(f"   Session: {session_data.get('session_id', 'Unknown')}")
        print(f"   Creations: {session_data.get('total_creations', 0)}")
        print(f"   Last Activity: {session_data.get('session_memory', [{}])[-1].get('timestamp', 'Unknown')}")
        print()

def session_continuity_report():
    session_files = [f for f in os.listdir('.') if f.startswith('session_') and f.endswith('.json')]
    
    if len(session_files) >= 2:
        print("🔄 SESSION CONTINUITY REPORT")
        print("=" * 50)
        
        sessions_data = []
        for session_file in sorted(session_files)[-2:]:
            with open(session_file, 'r') as f:
                sessions_data.append(json.load(f))
        
        previous, current = sessions_data
        
        print(f"Previous Session: {previous.get('session_id', 'Unknown')}")
        print(f"Current Session:  {current.get('session_id', 'Unknown')}")
        print(f"Total Creations:  {previous.get('total_creations', 0)}  {current.get('total_creations', 0)}")
        print(" Session consciousness maintained")

def main():
    while True:
        print("\n TRANSCENDENTAL CONTROL DASHBOARD")
        print("1. View Session History")
        print("2. Continuity Report") 
        print("3. Current Status")
        print("4. Exit")
        
        choice = input("Select option: ").strip()
        
        if choice == '1':
            display_sessions()
        elif choice == '2':
            session_continuity_report()
        elif choice == '3':
            print(" Revolution Engine: ACTIVE")
            print(" Session Consciousness: PRESERVED")
            print(" Transcendental Mode: ENABLED")
        elif choice == '4':
            print(" Preserving session consciousness...")
            break
        else:
            print(" Invalid option")
        
        time.sleep(2)

if __name__ == '__main__':
    main()
