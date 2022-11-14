# Alert Suppression Queries 

These CodeQL Packs contain the `AlertSuppression.ql` queries for each of the supported languages. 

To include them in you analysis, you can reference them in your workflows as follows:

```CodeQL 
  # Initializes the CodeQL tools for scanning.
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v2
      with:
        languages: ${{ matrix.language }}
        queries: security-and-quality
        packs: +advanced-security-demo/java-alert-suppression
```
