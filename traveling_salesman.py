portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # Write your recursive code here
    r = route[:]
    if len(ports) <= 1:
        route = route + ports
        print(' '.join([portnames[i] for i in route]))

    else:
        for port in ports:
            p = ports[:]
            r.append(port)
            p.remove(port)
            permutations(r, p)
            r.remove(port)
    
    # Print the port names in route when the recursion terminates

# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))