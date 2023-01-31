#pip install translator - translate

import translate 
from translate import Translator

data = Translator(from_lang="French", to_lang="English")
res = data.translate("merci")
print(res)