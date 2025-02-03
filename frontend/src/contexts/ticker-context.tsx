import { createContext, useContext, useState, ReactNode } from "react"

type TickerContextType = {
  globalTicker: string
  setGlobalTicker: (ticker: string) => void
}

const TickerContext = createContext<TickerContextType | undefined>(undefined)

export function TickerProvider({ children }: { children: ReactNode }) {
  const [globalTicker, setGlobalTicker] = useState("AAPL")

  return (
    <TickerContext.Provider value={{ globalTicker, setGlobalTicker }}>
      {children}
    </TickerContext.Provider>
  )
}

export function useTickerContext() {
  const context = useContext(TickerContext)
  if (context === undefined) {
    throw new Error("useTickerContext must be used within a TickerProvider")
  }
  return context
}
