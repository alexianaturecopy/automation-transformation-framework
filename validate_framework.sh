#!/bin/bash
echo "═══════════════════════════════════════════════════════"
echo "  AUTOMATION TRANSFORMATION FRAMEWORK - VALIDATION"
echo "═══════════════════════════════════════════════════════"
echo ""

# Check files exist
echo "✓ Checking core files..."
files=("README.md" "FRAMEWORK.md" "QUICKSTART.md" "IMPLEMENTATION_COMPLETE.md" "LICENSE" ".gitignore")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✓ $file exists"
    else
        echo "  ✗ $file MISSING"
    fi
done

echo ""
echo "✓ Checking architecture files..."
if [ -f "architecture/current_state.md" ]; then
    echo "  ✓ architecture/current_state.md exists"
fi

echo ""
echo "✓ Checking implementation files..."
if [ -f "implementation/roadmap.md" ]; then
    echo "  ✓ implementation/roadmap.md exists"
fi

echo ""
echo "✓ Checking business cases..."
if [ -f "business_cases/sales_to_cash.md" ]; then
    echo "  ✓ business_cases/sales_to_cash.md exists"
fi

echo ""
echo "✓ Checking data files..."
for csv in data/*.csv; do
    if [ -f "$csv" ]; then
        lines=$(wc -l < "$csv")
        echo "  ✓ $(basename $csv): $lines lines"
    fi
done

echo ""
echo "✓ Word counts..."
total_words=$(find . -name "*.md" -exec cat {} + | wc -w)
echo "  Total documentation: $total_words words"

echo ""
echo "✓ Repository size..."
du -sh .

echo ""
echo "═══════════════════════════════════════════════════════"
echo "  ✅ VALIDATION COMPLETE!"
echo "═══════════════════════════════════════════════════════"
