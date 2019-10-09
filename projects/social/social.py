# person - vertex
# connection - edge
# if person 1 is friends with person 2, person 2 is also friends with person 1 - bi-directional

import random

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        run_count = 0

        max_friends = round(numUsers / avgFriendships)
        if numUsers < avgFriendships:
            print("Please make sure your user count is greater than the average count")
            return None
        else:
            users = []
            # Add users
            for number in range(numUsers):
                self.addUser(number + 1)
                users.append(number + 1)
            # Create friendships

            for user_id in users:
                # add x number of friends, where x is a random num in range 0 to round(numUsers / avgFriendships)
                for x in range(random.randrange(0, stop = avgFriendships + 1)):
                    random.shuffle(users)
                    # call addFriendship(number, x)
                    if user_id < users[x]:
                        self.addFriendship(user_id, users[x])
                        run_count += 1
                        # add users[x] to visited to ensure it's not revisited

        print(f"************Ran addFriendship {run_count} times")
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        visited = {}

        q.enqueue([userID])

        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                visited[vertex] = path


            for neighbor in self.friendships[vertex]:
                if neighbor not in visited:
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    # sg.populateGraph(1000, 20)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
