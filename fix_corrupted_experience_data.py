"""
Script to fix Experience end_date fields that contain template syntax literals.
Run this on PythonAnywhere after pulling the latest code.

Usage: python fix_corrupted_experience_data.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from portfolio.models import Experience

def fix_corrupted_dates():
    """Fix any Experience records with template syntax in end_date field."""
    
    print("=" * 60)
    print("FIXING CORRUPTED EXPERIENCE DATA")
    print("=" * 60)
    
    experiences = Experience.objects.all()
    fixed_count = 0
    
    for exp in experiences:
        # Check if end_date contains template syntax
        if '{{' in exp.end_date or '}}' in exp.end_date or 'exp.end_date' in exp.end_date:
            print(f"\n❌ CORRUPTED DATA FOUND:")
            print(f"   Company: {exp.company}")
            print(f"   Position: {exp.position}")
            print(f"   Current end_date: {repr(exp.end_date)}")
            
            # Determine correct end date based on context
            # You can customize these mappings based on your actual data
            if 'attijari' in exp.company.lower() or 'payment' in exp.company.lower():
                correct_end_date = 'July 2025'
            elif 'bc skills' in exp.company.lower() or exp.company == 'BC SKILLS':
                correct_end_date = 'May 2024'
            else:
                # Default to "Present" for unknown entries
                correct_end_date = 'Present'
            
            # Update the record
            exp.end_date = correct_end_date
            exp.save()
            
            print(f"   ✅ FIXED! New end_date: {correct_end_date}")
            fixed_count += 1
        else:
            print(f"✓ {exp.company}: {exp.end_date} (OK)")
    
    print("\n" + "=" * 60)
    if fixed_count > 0:
        print(f"✅ SUCCESS! Fixed {fixed_count} corrupted record(s)")
    else:
        print("✅ No corrupted data found. All records are clean!")
    print("=" * 60)

if __name__ == '__main__':
    fix_corrupted_dates()
