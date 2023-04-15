# START
# -------------------------------------------------------------------------------
# using 1 for loop
# n=5
# for i in range(1,n+1):
#     print(i*"* ")

# using 2 for loop
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("* ", end="")
#     print()

# using 2 while loop
# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("* ", end="")
#         j +=1
#     i +=1
#     print()

# OUTPUT
# *
# * *
# * * *
# * * * *
# * * * * *

# -------------------------------------------------------------------------------
# n=5
# for i in range(1,n+1):
#     print((n-(i-1))*"* ")


# n=5
# for i in range(1,n+1):
#     for j in range((n-(i-1))):
#         print("* ", end="")
#     print()


# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=(n-(i-1)):
#         print("* ", end="")
#         j +=1
#     i +=1
#     print()

# OUTPUT
# * * * * *
# * * * *
# * * *
# * *
# *

# -------------------------------------------------------------------------------
# n=5
# for i in range(1,n+1):
#     print((n-i)*"  "+i*"* ")

# n=5
# for i in range(1,n+1):
#     for j in range((n-i)):
#         print("  ", end="")
#     for j in range(i):
#         print("* ", end="")
#     print()

# OUTPUT
#         *
#       * *
#     * * *
#   * * * *
# * * * * *


# -------------------------------------------------------------------------------
# n=5
# for i in range(1,n+1):
#     print((i-1)*"  "+(n-(i-1))*"* ")

# n=5
# for i in range(1,n+1):
#     for j in range((i-1)):
#         print("  ", end="")
#     for j in range((n-(i-1))):
#         print("* ", end="")
#     print()

# OUTPUT
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# -------------------------------------------------------------------------------
# n=5
# for i in range(1,n+1):
#     print((i-1)*"  "+(n-(i-1))*"* ")

# OUTPUT
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# ---------------------------------------------------------------
# n=9
# for i in range(1,n+1):
#     if i <= 5:
#         print(i*"* ")
#     else:
#         print(((n+1)-i) * "* ")
    
# n=9
# for i in range(1,(n+1)):
#     if i <=5:
#         for j in range(i):
#             print("*",end=" ")
#         print()
#     else:
#         for j in range((n + 1) - i):
#             print("*", end=" ")
#         print()


# OUTPUT

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# -------------------------------------------------------------------------------

# n=9
# for i in range(1,n+1):
#     if i <= 5:
#         print(((n-4)-i)*"  "+i*"* ")
#     else:
#         print((i-(n-4))*"  "+((n+1)-i)*"* ")

# n=9
# for i in range(1,(n+1)):
#     if i <=5:
#         for j in range(((n-4)-i)):
#             print(end="  ")
#         for j in range(i):
#             print("* ",end="")
#         print()
#     else:
#         for j in range(i-(n-4)):
#             print(end="  ")
#         for j in range((n+1)-i):
#             print("* ", end="")
#         print()

# OUTPUT

#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# -------------------------------------------------------------------------------

# n=9
# for i in range(1,n+1):
#     if i <= 5:
#         print(((n-4)-i)*"  "+i*"* "+(i-1)*"* ")
#     else:
#         print((i-(n-4))*"  "+((n+1)-i)*"* "+(n-i)*"* ")

# n=9
# for i in range(1,(n+1)):
#     if i <=5:
#         for j in range(((n-4)-i)):
#             print(end="  ")
#         for j in range(i):
#             print("* ",end="")
#         for j in range(i-1):
#             print("* ",end="")
#         print()
#     else:
#         for j in range(i-(n-4)):
#             print(end="  ")
#         for j in range((n+1)-i):
#             print("* ", end="")
#         for j in range(n-i):
#             print("* ",end="")
#         print()

# Output
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *


# -------------------------------------------------------------------------------
# n=5
# for i in range(1,n+1):
#     print((n-i)*"  "+i*"* "+(i-1)*"* ")

# n=5
# for i in range(1,n+1):
#     for j in range((n-i)):
#         print("  ", end="")
#     for j in range(i):
#         print("* ", end="")
#     for j in range((i-1)):
#         print("* ", end="")
#     print()

# OUTPUT
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *




# -------------------------------------------------------------------------------
# n=5
# for i in range(1,n+1):
#     print((i-1)*"  "+(2*(n-i)+1)*"* ")

# n=5
# for i in range(1,n+1):
#     for j in range((i-1)):
#         print(end="  ")
#     for j in range(2*(n-i)+1):
#         print("* ", end="")
#     print()

# OUTPUT
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# -------------------------------------------------------------------------------
# n=9
# for i in range(1,n+1):
#     if i<=5:
#         print((n-4-i)*"  "+i*"* "+(i-1)*"* ")
#     else:
#         print((i-(n-4)) * "  " + (n+1-i) * "* " + (n-i) * "* ")

# OUTPUT
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# -------------------------------------------------------------------------------
# n=9
# for i in range(1,n+1):
#     if i<=5:
#         print((i-1)*"  "+(n-2*(i-1))*"* ")
#     else:
#         print((n-i) * "  " + (2*i-n) * "* ")

# n=9
# for i in range(1,(n+1)):
#     if i <=5:
#         for j in range(i-1):
#             print(end="  ")
#         for j in range(n-2*(i-1)):
#             print("* ",end="")
#         print()
#     else:
#         for j in range(n-i):
#             print(end="  ")
#         for j in range(2*i-n):
#             print("* ", end="")
#         print()

# OUTPUT
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


# -------------------------------------------------------------------------------
# n=5
# for i in range(1,n+1):
#     print((i-1)*"  "+n*"* ")
# n=5
# for i in range(1,n):
#     for j in range(i-1):
#         print(end="  ")
#     for j in range(n):
#         print("* ",end="")
#     print()

# OUTPUT
# * * * * *
#   * * * * *
#     * * * * *
#       * * * * *
#         * * * * *


# -------------------------------------------------------------------------------
# n=5
# for i in range(1,n+1):
#     print((n-i)*"  "+n*"* ")

# n=5
# for i in range(1,n):
#     for j in range(n-i):
#         print(end="  ")
#     for j in range(n):
#         print("* ",end="")
#     print()


# OUTPUT
#         * * * * *
#       * * * * *
#     * * * * *
#   * * * * *
# * * * * *


# -------------------------------------------------------------------------------

