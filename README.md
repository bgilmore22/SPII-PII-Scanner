This is a scanner that is built to process either a docx or pdf file and look for any SPII or PII information.
If any of this information is found in the text, the scanner will replace it with [REDACTED] so that no information is given out.
The scanner will also keep track of how many occurences a SPII or PII information piece shows up so that it can assign a file a risk rating.
Finally, it will return the file with all SPII and PII information replaced with [REDACTED] and will change the file name to include '_redacted' at the end.
