import argparse
import sys
from colorama import Fore, Style, init
import Methods

init()

BANNER = r"""
 .'"'.        ___,,,___        .'``.
: (\  `."'"```         ```"'"-'  /) ;
 :  \                         `./  .'
  `.                            :.'
    /        _         _        \

   |         0}       {0         |
   |         /         \         |        ____  _________    ____     ____  ____  ____  _____    
   |        /           \        |       / __ )/ ____/   |  / __ \   / __ \/ __ \/ __ \/ ___/   
   |       /             \       |      / __  / __/ / /| | / /_/ /  / / / / / / / / / /\__ \
    \     |      .-.      |     /      / /_/ / /___/ ___ |/ _, _/  / /_/ / /_/ / /_/ /___/ / 
     `.   | . . /   \ . . |   .'      /_____/_____/_/  |_/_/ |_|  /_____/_____/\____//____/ 
       `-._\.'.(     ).'./_.-'
           `\'  `._.'  '/'
             `. --'-- .'
               `-...-'
"""

def main():
    print(Fore.YELLOW + BANNER + Style.RESET_ALL)
    
    parser = argparse.ArgumentParser(description="Bear DDoS - Stress and Load Testing Tool")
    
    parser.add_argument("--url", required=True, help="Target URL address to test")
    parser.add_argument("--method", choices=["A", "S"], required=True, help="Attack Method: A (Async), S (Sync)")
    parser.add_argument("-T", type=int, default=1, dest="thread", help="Number of Threads / Concurrent Tasks (Default: 1)")
    parser.add_argument("--random-user", action="store_true", help="Enable random User-Agent and Fake IP spoofing")
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
        
    args = parser.parse_args()
    
    print(Fore.BLUE + f"[*] Target URL: {args.url}")
    print(f"[*] Selected Method: {args.method}")
    print(f"[*] Power (Threads/Tasks): {args.thread}")
    print(f"[*] Random User & Fake IP: {args.random_user}\n" + Style.RESET_ALL)
    
    try:
        if args.method == "S":
            if args.random_user:
                Methods.S_Method_ru(args.url, args.thread)
            else:
                Methods.S_Method(args.url, args.thread, False)
                
        elif args.method == "A":
            if args.random_user:
                Methods.A_Method_ru(args.url, args.thread)
            else:
                Methods.A_Method(args.url, args.thread, False)
            
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Execution cancelled by user. Bear is returning to hibernation..." + Style.RESET_ALL)
        sys.exit(0)

if __name__ == "__main__":
    main()
