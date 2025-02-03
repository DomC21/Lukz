import { useState, useEffect } from "react"
import { useTickerContext } from "@/contexts/ticker-context"
import { Input } from "@/components/ui/input"
import {
  Command,
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command"
import { Search } from "lucide-react"

const commonTickers = ["AAPL", "TSLA", "GOOGL", "MSFT", "AMZN", "META", "NVDA", "AMD", "INTC", "JPM"]

export function GlobalTickerSearch() {
  const { globalTicker, setGlobalTicker } = useTickerContext()
  const [open, setOpen] = useState(false)
  const [search, setSearch] = useState("")
  const [suggestions, setSuggestions] = useState<string[]>([])

  useEffect(() => {
    if (search.length > 0) {
      setSuggestions(
        commonTickers.filter(ticker => 
          ticker.toLowerCase().includes(search.toLowerCase())
        )
      )
    } else {
      setSuggestions([])
    }
  }, [search])

  return (
    <div className="relative w-full max-w-sm">
      <div className="relative">
        <Search className="absolute left-2 top-2.5 h-4 w-4 text-brand-gray-400" />
        <Input
          placeholder="Search ticker (e.g. AAPL)"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          onFocus={() => setOpen(true)}
          className="pl-8 bg-brand-gray-900 border-brand-gray-700 text-brand-gray-100 focus:border-brand-cyan focus:ring-brand-cyan/20"
        />
      </div>
      {open && suggestions.length > 0 && (
        <div className="absolute top-full left-0 right-0 mt-1 bg-brand-gray-900 border border-brand-gray-700 rounded-md shadow-lg">
          <Command>
            <CommandList>
              <CommandGroup>
                {suggestions.map((ticker) => (
                  <CommandItem
                    key={ticker}
                    onSelect={() => {
                      setGlobalTicker(ticker)
                      setSearch("")
                      setOpen(false)
                    }}
                    className="text-brand-gray-100 hover:bg-brand-gray-800 cursor-pointer p-2"
                  >
                    {ticker}
                  </CommandItem>
                ))}
              </CommandGroup>
            </CommandList>
          </Command>
        </div>
      )}
    </div>
  )
}
