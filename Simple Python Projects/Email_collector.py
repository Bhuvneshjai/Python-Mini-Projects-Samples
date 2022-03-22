# The task you have to perform is "Email Extractor."

# Suppose you are a student and want to get an internship.
# You have to contact your professors and some companies to get an
# internship. For that, you need their email so that you can contact
# them.

# The task you have to do is to extract the email from text data
# using Regex Expressions.

# When you go to a website and click on the contact section, by
# pressing CTRL+A,
# all the website's content gets added to the clipboard. ' \
# Paste the data in your python file or in a string.
# Extract an email from the above data, and after extracting
# the email, write it into a file with a new line character.' \
# ' Your text file after writing data should look similar to this:

import re
str_data = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Habitant morbi tristique senectus et netus et malesuada fames.
Phasellus egestas tellus rutrum tellus pellentesque eu tincidunt. 
Convallis a cras semper auctor neque vitae tempus quam pellentesque. 
Sagittis id consectetur purus ut faucibus pulvinar. Morbi tristique
senectus et netus et malesuada fames ac turpis. Semper eget duis at
tellus at urna condimentum. Nulla posuere sollicitudin aliquam
ultrices sagittis orci a scelerisque. Bibendum ut tristique et 
egestas quis ipsum suspendisse. In egestas erat imperdiet sed 
euismod. Nec tincidunt praesent semper feugiat nibh sed pulvinar
proin. Euismod elementum nisi quis eleifend quam adipiscing.

Nulla facilisi cras fermentum odio eu feugiat pretium nibh ipsum. 
Duis at tellus at urna. Vulputate mi sit amet mauris commodo quis 
imperdiet massa tincidunt. Sed viverra ipsum nunc aliquet. Lorem sed
risus ultricies tristique nulla aliquet enim tortor at. Consequat
mauris nunc congue nisi vitae suscipit tellus mauris a. Feugiat 
sed lectus vestibulum mattis ullamcorper velit. Lorem sed risus
ultricies tristique nulla aliquet enim. Ipsum faucibus vitae
aliquet nec ullamcorper sit amet risus nullam. Eget aliquet
nibh praesent tristique magna sit amet. Nisi est sit amet facilisis 
magna etiam tempor orci. Volutpat diam ut venenatis tellus in metus.
Volutpat diam ut venenatis tellus in metus vulputate. Auctor elit sed 
vulputate mi sit amet. Et netus et malesuada fames ac turpis egestas 
maecenas. Porta lorem mollis aliquam ut porttitor leo a diam 
sollicitudin.

Commodo odio aenean sed adipiscing. At tellus at urna condimentum 
mattis pellentesque id nibh tortor. Ultrices dui sapien eget mi. 
Nulla facilisi etiam dignissim diam. Eu facilisis sed odio morbi quis 
commodo odio aenean. Diam donec adipiscing tristique risus nec. 
Pellentesque id nibh tortor id aliquet lectus proin. Faucibus nisl 
tincidunt eget nullam non nisi. Eu tincidunt tortor aliquam nulla 
facilisi cras. Dictum at tempor commodo ullamcorper a lacus vestibulum 
sed. Amet commodo nulla facilisi nullam vehicula ipsum. Eu scelerisque 
felis imperdiet proin fermentum leo vel. Auctor augue mauris augue neque 
gravida in fermentum.

Euismod nisi porta lorem mollis aliquam. Nullam ac tortor vitae purus 
faucibus. Ut consequat semper viverra nam libero justo laoreet. 
Commodo viverra maecenas accumsan lacus. Libero nunc consequat interdum 
varius sit amet mattis vulputate enim. Nulla porttitor massa id neque 
aliquam. Risus feugiat in ante metus dictum at tempor. Vulputate sapien 
nec sagittis aliquam malesuada bibendum arcu vitae. Eu consequat ac 
felis donec et odio pellentesque diam volutpat. In metus vulputate eu 
scelerisque. Neque viverra justo nec ultrices dui sapien eget mi. 
Accumsan in nisl nisi scelerisque eu ultrices. Augue lacus viverra 
vitae congue. Viverra accumsan in nisl nisi scelerisque eu ultrices 
vitae auctor. Feugiat sed lectus vestibulum mattis ullamcorper velit. 
Suspendisse potenti nullam ac tortor.

Phasellus egestas tellus rutrum tellus. Facilisi cras fermentum odio eu 
feugiat. Enim blandit volutpat maecenas volutpat blandit aliquam etiam. 
Aliquam faucibus purus in massa tempor nec feugiat. Condimentum vitae 
sapien pellentesque habitant morbi tristique. Viverra nam libero justo 
laoreet sit. Purus faucibus ornare suspendisse sed. Nullam non nisi est 
sit amet facilisis magna. Libero justo laoreet sit amet cursus sit. 
Morbi tempus iaculis urna id volutpat. Vel risus commodo viverra 
maecenas accumsan lacus vel facilisis volutpat. Orci a scelerisque 
purus semper eget duis at tellus. Tortor consequat id porta nibh. 
Quam elementum pulvinar etiam non quam lacus suspendisse faucibus 
interdum. Nulla porttitor massa id neque aliquam vestibulum morbi 
blandit. Vitae tortor condimentum lacinia quis vel eros. Ornare lectus 
sit amet est placerat in egestas erat.
example@email.com
pakhi.bisht@example.com
"""
list1 = re.findall(r'[a-zA-Z0-9./+%]+@[a-z.]+[.][a-z]+',str_data)
for email in list1:
    print(f"Email ID - {email}")
