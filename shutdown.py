import platform
import subprocess


def shutdown():
   answer = input("Are you sure you want to shut down the system? (yes/no): ")

   if answer.strip().lower() != "yes":
      print("sorry")
      return

   print("shutting down")
   system = platform.system()
   if system == "Windows":
      command = ["shutdown", "/s", "/t", "0"]
   elif system in {"Linux", "Darwin"}:
      command = ["shutdown", "-h", "now"]
   else:
      print(f"Shutdown is not supported on {system}.")
      return

   print("Shutting down the system...")
   subprocess.run(command, check=True)


if __name__ == "__main__":
   shutdown()


