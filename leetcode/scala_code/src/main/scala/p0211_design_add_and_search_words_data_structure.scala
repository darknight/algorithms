import scala.collection.mutable

class WordDictionary() {

  private val trie = new Trie()

  def addWord(word: String) {
    trie.add(word)
  }

  def OOM_search(word: String): Boolean = {
    var found = false
    def fillDot(prefix: String, suffix: String): Unit = {
      if (found) return
      if (suffix.isEmpty) {
        found = trie.contains(prefix)
        return
      }
      if (suffix.contains('.')) {
        val tmp = suffix.takeWhile(_ != '.')
        val newSuffix = suffix.drop(tmp.length + 1)
        for (c <- 'a' to 'z') {
          fillDot(prefix + tmp + c, newSuffix)
        }
      } else {
        fillDot(prefix + suffix, "")
      }
    }
    fillDot("", word)
    found
  }

  // refer to https://leetcode.com/problems/design-add-and-search-words-data-structure/solutions/1725327/java-c-python-a-very-well-detailed-explanation/
  def search(word: String): Boolean = {
    def _search(root: Node, w: String): Boolean = {
      var curr = Option(root)
      for ((c, idx) <- w.iterator.zipWithIndex if curr.nonEmpty) {
        if (c == '.') {
          return curr.get.children.values.exists(node => _search(node, w.substring(idx+1)))
        }
        curr = curr.get.children.get(c)
      }
      curr.exists(_.isEndingChar)
    }

    _search(trie.root, word)
  }
}

class Node(var isEndingChar: Boolean,
           val children: mutable.Map[Char, Node] = mutable.Map())

class Trie() {


  val root = new Node(false)

  def add(s: String): Unit = {
    var current = root
    for (c <- s) current = current.children.getOrElseUpdate(c, new Node(false))
    current.isEndingChar = true
  }

  def contains(s: String): Boolean = {
    var current = Option(root)
    for (c <- s if current.nonEmpty) current = current.get.children.get(c)
    current.exists(_.isEndingChar)
  }

  def prefixesMatchingString0(s: String): Set[Int] = {
    var current = Option(root)
    val output = Set.newBuilder[Int]
    for ((c, i) <- s.zipWithIndex if current.nonEmpty) {
      if (current.get.isEndingChar) output += i
      current = current.get.children.get(c)
    }
    if (current.exists(_.isEndingChar)) output += s.length
    output.result()
  }

  def prefixesMatchingString(s: String): Set[String] = {
    prefixesMatchingString0(s).map(s.substring(0, _))
  }

  def stringsMatchingPrefix(s: String): Set[String] = {
    var current = Option(root)
    for (c <- s if current.nonEmpty) current = current.get.children.get(c)
    if (current.isEmpty) Set()
    else {
      val output = Set.newBuilder[String]
      def recurse(current: Node, path: List[Char]): Unit = {
        if (current.isEndingChar) output += (s + path.reverse.mkString)
        for ((c, n) <- current.children) recurse(n, c :: path)
      }
      recurse(current.get, Nil)
      output.result()
    }
  }
}

object Test {
  def main(args: Array[String]): Unit = {
    val wordDictionary = new WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    println(wordDictionary.search("pad"))// return False
    println(wordDictionary.search("bad")) // return True
    println(wordDictionary.search(".ad")) // return True
    println(wordDictionary.search("b..")) // return True
  }
}
