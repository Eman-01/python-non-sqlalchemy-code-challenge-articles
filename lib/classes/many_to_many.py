class Article:
    all = [] 
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self) 
    
    
    def get_author(self):
        return self._author

    
    def set_author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")
        self._author = author
    author=property(get_author,set_author)
    
    def get_magazine(self):
        return self._magazine

    
    def  set_magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        self._magazine = magazine 

    magazine=property(get_magazine,set_magazine)
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if hasattr(self, '_title'):
            print("Cannot change the title after the article is instantiated.")
        elif isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            print("Title must be a string between 5 and 50 characters, inclusive.")

    title = property(get_title, set_title)   
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must have more than 0 characters")
        
        self._name = name
        self._articles = []
        self._magazines = []
        
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        raise ValueError("Cannot change authors name")


    def articles(self):
        return [article for article in Article.all if article.author == self]
        

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
       categories = {article.magazine.category for article in Article.all if article.author == self}
       return list(categories) if categories else None

class Magazine:
    _all_magazines = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            print("Name must be a string between 2 and 16 characters, inclusive.")

    name = property(get_name, set_name)

    def get_category(self):
        return self._category
    
    def set_category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            print("Category must be a non-empty string.")


    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        

    def contributors(self):
        return list({article.author for article in self.articles()})
        

    def article_titles(self):
      if not self._articles:
            return None
      return [article.title for article in self._articles]  

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        
        return [author for author, count in author_counts.items() if count > 2] if author_counts else None
        
    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles), default=None)