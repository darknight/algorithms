object StringCompress extends App {

  def stringCompress(str: String): String = {
    def _f(s: List[(Char, Int)]): List[(Char, Int)] = {
      s match {
        case h1 :: h2 :: tail =>
          if(h1._1 == h2._1) _f((h1._1, h1._2 + 1) :: tail)
          else h1 :: _f(h2 :: tail)
        case _ => s
      }
    }
    val res = _f(str.map(c => (c, 1)).toList)
    res.foldLeft("") {
      (acc: String, t: Tuple2[Char, Int]) =>
        if(t._2 == 1) acc + t._1
        else acc + t._1 + t._2
    }
  }

  override def main(args: Array[String]): Unit = {
    io.Source.stdin.getLines().foreach(line => println(stringCompress(_)))
    println(stringCompress("zzz"))
    println(stringCompress("abcaaabbb"))
    println(stringCompress("abcd"))
    println(stringCompress("aaabaaaaccaaaaba"))
  }
}
