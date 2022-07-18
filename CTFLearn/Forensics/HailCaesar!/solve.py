#string = '/<V5;)j}j6\<Y)8><\9Fbu,Hy4ONC}pxP"4st12wn`?@O$6BgQo7i#gtD|s>3lf='
#string = "SWYgeW91IGFyZSBoYXZpbmcgdHJvdWJsZSBzb2x2aW5nIHRoaXMgY2hhbGxlbmdlLCBwbGVhc2Ugc29sdmUgbXkgb3RoZXIKY2hhbGxlbmdlcyBmaXJzdDoKUnViYmVyRHVjawpTbm93Ym9hcmQKUGlrZXNQZWFrCkdhbmRhbGZUaGVXaXNlCgpUaGUgY2hhbGxlbmdlcyBhcmUgZGVzaWduZWQgdG8gYmUgaW5jcmVhc2luZyBpbiBkaWZmaWN1bHR5IGFuZCB0aGlzIEhhaWxDYWVzYXIgY2hhbGxlbmdlIGlzIHRoZSBuZXh0CmNoYWxsZW5nZSBpbiB0aGUgc2VyaWVzLgoKTXkgVHdpdHRlciBETSBpcyBvcGVuIEBrY2Jvd2h1bnRlciBidXQgcGxlYXNlIG9ubHkgcGluZyBtZSBpZiB5b3UgaGF2ZSBzb2x2ZWQgdGhlIGFib3ZlIGNoYWxsZW5nZXMgZmlyc3QuCgpJZiB5b3UgYXJlIG5ldyB0byB0aGUganBlZyBmaWxlIGZvcm1hdCBwbGVhc2UgcmVhZCB0aGlzOgpodHRwczovL2Rldi5leGl2Mi5vcmcvcHJvamVjdHMvZXhpdjIvd2lraS9UaGVfTWV0YWRhdGFfaW5fSlBFR19maWxlcwoKSWYgeW91IGFyZSBuZXcgdG8gaGFja2luZyBhbmQgYXJlIHN0aWxsIGxlYXJuaW5nIGFib3V0IGJpdHMgYW5kIGJ5dGVzIHBsZWFzZSB3YXRjaCB0aGlzIHZpZGVvOgpodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PXRMZHZFT2FtM3NrCgp4b3JwZCBoYXMgYSBsb3Qgb2YgZnJlZSB2aWRlb3MgdGhhdCB0ZWFjaCBpbXBvcnRhbnQgY29tcHV0ZXIgc2NpZW5jZSAvIGhhY2tpbmcgY29uY2VwdHMuCgpOb3RlIHRoYXQgb2Z0ZW4gbXkgY2hhbGxlbmdlcyBjb21iaW5lIGZvcmVuc2ljcyBhbmQgc29tZSBhc3BlY3Qgb2YgY3J5cHRvZ3JhcGh5LgoKSGF2ZSBmdW4hCmtjYm93aHVudGVyCgoK"
string = '2m{y!"%w2z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0'

res = ""
for i in range(1, 95):
	for j in string:
		loc = ord(j)
		loc += i
		if loc > 126:
			loc = loc%126
			loc = loc+31
		res += chr(loc)
	print(res)
	res = ""
	print("\n\n")
