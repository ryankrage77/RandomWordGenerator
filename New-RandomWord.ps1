# Ryankrage77's Random Word Generator - Powershell Edition
# Generates random pronouncable strings of a specified length.

$Word          = [System.Collections.ArrayList]@()
$Alphabet      = "abcdefghijklmnopqrstuvwxyz" -split ""
$Vowels        = "aeiou" -split ""
$CurrentLetter = ""
$GenLength     = 0

while ($true) {
  $StringLength = Read-Host -Prompt "String length"
  while ($GenLength -le [int]$StringLength - 1) {
    $CurrentLetter = Get-Random $Alphabet
    if ($CurrentLetter -in $Vowels) {
      if ($GenLength -ge 3) {
        if ($Word[($GenLength - 1)] -in $Vowels -and $Word[($GenLength - 2)] -in $Vowels -and $Word[($GenLength - 3)] -in $Vowels) {
          #Write-Host "Letter rejected, more than 3 vowels in a row"
          continue
        }
      }
      [void]$Word.Add($CurrentLetter)
      $GenLength += 1
      #Write-Host $Word
    } else {
      if ($GenLength -ge 2) {
        if ($Word[$GenLength - 1] -notin $Vowels -and $Word[$GenLength - 2] -notin $Vowels) {
          #Write-Host "Letter rejected, more than 2 consonants in a row"
          continue
        }
      }
      [void]$Word.Add($CurrentLetter)
      $GenLength += 1
      #Write-Host $Word
    }
  }

  $Word[0] = $Word[0].ToUpper()
  $FullWord = $Word -join ""
  Write-Host "Generated Word: $FullWord"
  $GenLength = 0
  $Word = [System.Collections.ArrayList]@()
  continue
}
