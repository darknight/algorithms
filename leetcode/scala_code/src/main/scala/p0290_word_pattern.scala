import scala.collection.mutable

object Solution {
  def wordPattern(pattern: String, s: String): Boolean = {
    val chars = pattern.toCharArray
    val terms = s.split(" ")
    if (terms.length != chars.length) {
      return false
    }

    val map = mutable.Map[Char, String]()
    val used = mutable.Set[String]()
    chars.zip(terms).foreach { case (ch, term) =>
      if (map.contains(ch)) {
        if (map(ch) != term) return false
      } else {
        if (used.contains(term)) return false
        map(ch) = term
        used.add(term)
      }
    }
    true
  }
}
