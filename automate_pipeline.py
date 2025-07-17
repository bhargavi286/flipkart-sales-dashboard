import argparse
import subprocess
def run_script(script_name):
    print(f"\n Running {script_name}...")
    subprocess.run(["python", script_name], check=True)
parser = argparse.ArgumentParser(description="Flipkart Data Analysis Pipeline")
parser.add_argument('--clean', action='store_true', help='Run data cleaning')
parser.add_argument('--eda', action='store_true', help='Run exploratory data analysis')
parser.add_argument('--report', action='store_true', help='Generate PDF report')
parser.add_argument('--all', action='store_true', help='Run all steps')
args = parser.parse_args()
if args.clean:
    run_script("data_cleaning.py")
if args.eda:
    run_script("eda_visualization.py")
if args.report:
    run_script("generate_report.py")
if args.all:
    run_script("data_integration.py")
    run_script("data_cleaning.py")
    run_script("eda_visualization.py")
    run_script("generate_report.py")
