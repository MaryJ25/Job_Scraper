import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()


def search(args):
    print(f"Looking for a {args.position} in {args.location} at {args.seniority} level.")


search_parser = subparsers.add_parser('search')
search_parser.add_argument('position', help='What position are you looking for? (type string)')
search_parser.add_argument('location', help='Where would you like to work? (type string)')
search_parser.add_argument('seniority', help='What seniority level? (type string)')
search_parser.set_defaults(func=search)

search_parser.add_argument('--email', default=None, help="add this option followed by your email address if you'd "
                                                         "like to receive the output as email")
search_parser.add_argument('--show', default=None, help="add this option if you'd like to see the output instead of "
                                                        "saving it")

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)