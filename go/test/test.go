package main

// autoformat-ignore (avoid gofmt changing line-endings, which should be specifically LFs here)

func main() {
	x := 42
	x = x // codeql
	x = x // codeql[go/redundant-assignment]
	x = x // codeql[go/redundant-assignment]
	x = x // codeql[go/redundant-assignment, go/redundant-operation]
	x = x // codeql[@tag:nullness]
	x = x // codeql[@tag:nullness,go/redundant-assignment]
	x = x // codeql[@expires:2017-06-11]
	x = x // codeql[go/redundant-operation] because I know better than codeql
	x = x // codeql: blah blah
	x = x // codeql blah blah #falsepositive
	x = x //codeql  [go/redundant-operation]
	x = x /* codeql */
	x = x // codeql[]
	x = x // codeqlfoo
	x = x //codeql
	x = x //	codeql
	x = x // codeql	[go/redundant-assignment]
	x = x // foocodeql[go/redundant-assignment]
	x = x // foocodeql
	x = x // foo; codeql
	x = x // foo; codeql[go/redundant-assignment]
	x = x // foo codeql
	x = x // foo codeql[go/redundant-assignment]
	x = x // foo codeql bar
	x = x // foo codeql[go/redundant-assignment] bar
	x = x // codeql!
	x = x // codeql[go/redundant-assignment]
	x = x // codeql[go/redundant-assignment] and codeql[go/redundant-operation]
	x = x // codeql[go/redundant-assignment]; codeql
	x = x /* codeql[] */
	x = x /* codeql[go/redundant-assignment] */
	x = x /* codeql
               */
	x = x /* codeql

               */
	x = x /* codeql[@tag:nullness,go/redundant-assignment] */
	x = x /* codeql[@tag:nullness] */
}
