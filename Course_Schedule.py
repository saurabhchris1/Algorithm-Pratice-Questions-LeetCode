# There are a total of numCourses courses you have to take,
# labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course
# 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite
# pairs, is it possible for you to finish all courses?


class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = {}

        for prereq in prerequisites:

            if prereq[0] in graph:
                graph[prereq[0]].append(prereq[1])

            else:
                graph[prereq[0]] = [prereq[1]]

        for course in range(numCourses):

            if self.isCyclic(graph, course, set(), {}):
                return False

        return True

    def isCyclic(self, graph, course, seen, cache):

        if course in cache:
            return cache[course]

        if course in seen:
            return True
        if course not in graph:
            return False

        seen.add(course)
        ret = False
        for neighbour in graph[course]:

            if self.isCyclic(graph, neighbour, seen, cache):
                ret = True
                break
        seen.remove(course)
        cache[course] = ret
        return ret
