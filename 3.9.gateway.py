# Phase 1: The Global State
current_user = "Guest"
is_authenticated = False


# Phase 2: Architecting the Decorator ... added Boss Level Challenge
def require_auth(func):
    # original
    # def wrapper():
    #     if is_authenticated == False:
    #         print("403 FORBIDDEN: Access Denied for Guest.")
    #         return is_authenticated
    #     elif is_authenticated == True:
    #         print("200 OK: Authentication verified.")
    #     func()
    # return wrapper

    # Boss Level Challenge Added
    def wrapper(*args, **kwargs):
        if not is_authenticated:
            print("403 FORBIDDEN: Access Denied for Guest.")
            return 
        else:
            print("200 OK: Authentication verified.")
        func(*args, **kwargs)
    return wrapper

# Phase 3: Deploying the Security Grid
@require_auth
def view_bak_vault():
    print("Opening Vault... Total balance is $50,000,000.")

@require_auth
def delete_database():
    print("Executing DROP TABLE... Database erased.")

@require_auth
def dowload_file(file_id):
    print(f"Dowloading file: {file_id}")



if __name__ == "__main__":
    print("--- Testing: Locked State ---")
    view_bak_vault()
    dowload_file("Balance_Sheet.pdf")

    print("\n--- Testing: Authenticated State ---")
    is_authenticated = True
    view_bak_vault()
    dowload_file("Balance_Sheet.pdf")