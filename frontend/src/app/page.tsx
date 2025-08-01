"use client"

import type React from "react"
import { useState, useEffect } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./components/ui/card"
import { Button } from "./components/ui/button"
import { Input } from "./components/ui/input"
import { Label } from "./components/ui/label"
import { Alert, AlertDescription } from "./components/ui/alert"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./components/ui/tabs"
import { Badge } from "./components/ui/badge"
import { BarChart3, Users, Trophy, Calendar, LogIn, Eye, EyeOff, Plus, Edit, Trash2 } from "lucide-react"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "./components/ui/dialog"

interface User {
  id: number
  username: string
  email: string
  full_name: string
  is_active: boolean
}

interface Team {
  id: number
  nombre: string
  ciudad: string
}

interface Stats {
  totalTeams: number
  totalPlayers: number
  totalMatches: number
  totalTournaments: number
}

interface NewTeam {
  nombre: string
  ciudad: string
}

export default function Dashboard() {
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [user, setUser] = useState<User | null>(null)
  const [teams, setTeams] = useState<Team[]>([])
  const [stats, setStats] = useState<Stats>({
    totalTeams: 0,
    totalPlayers: 0,
    totalMatches: 0,
    totalTournaments: 0,
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")
  const [showPassword, setShowPassword] = useState(false)
  const [showNewTeamDialog, setShowNewTeamDialog] = useState(false)
  const [newTeam, setNewTeam] = useState<NewTeam>({ nombre: "", ciudad: "" })

  // Login form state
  const [loginForm, setLoginForm] = useState({
    username: "",
    password: "",
  })

  useEffect(() => {
    const token = localStorage.getItem("access_token")
    if (token) {
      fetchUserData(token)
    }
  }, [])

  const fetchUserData = async (token: string) => {
    try {
      const response = await fetch("http://localhost:8000/users/me", {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      })

      if (response.ok) {
        const userData = await response.json()
        setUser(userData)
        setIsAuthenticated(true)
        await fetchDashboardData(token)
      } else {
        localStorage.removeItem("access_token")
        setIsAuthenticated(false)
      }
    } catch (error) {
      console.error("Error fetching user data:", error)
      localStorage.removeItem("access_token")
      setIsAuthenticated(false)
    }
  }

  const fetchDashboardData = async (token: string) => {
    try {
      // Fetch teams
      const teamsResponse = await fetch("http://localhost:8000/teams/", {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      })

      if (teamsResponse.ok) {
        const teamsData = await teamsResponse.json()
        setTeams(teamsData)
        setStats((prev) => ({ ...prev, totalTeams: teamsData.length }))
      }

      // Mock data for other stats
      setStats((prev) => ({
        ...prev,
        totalPlayers: 150,
        totalMatches: 45,
        totalTournaments: 3,
      }))
    } catch (error) {
      console.error("Error fetching dashboard data:", error)
    }
  }

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError("")

    try {
      const response = await fetch("http://localhost:8000/auth/login-json", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(loginForm),
      })

      if (response.ok) {
        const data = await response.json()
        localStorage.setItem("access_token", data.access_token)
        await fetchUserData(data.access_token)
        setLoginForm({ username: "", password: "" })
      } else {
        const errorData = await response.json()
        setError(errorData.detail || "Login failed")
      }
    } catch (error) {
      setError("Network error. Please try again.")
    } finally {
      setLoading(false)
    }
  }

  const handleCreateTeam = async (e: React.FormEvent) => {
    e.preventDefault()
    const token = localStorage.getItem("access_token")
    if (!token) return

    try {
      const response = await fetch("http://localhost:8000/teams/", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newTeam),
      })

      if (response.ok) {
        const createdTeam = await response.json()
        setTeams((prev) => [...prev, createdTeam])
        setStats((prev) => ({ ...prev, totalTeams: prev.totalTeams + 1 }))
        setNewTeam({ nombre: "", ciudad: "" })
        setShowNewTeamDialog(false)
      } else {
        const errorData = await response.json()
        setError(errorData.detail || "Failed to create team")
      }
    } catch (error) {
      setError("Network error. Please try again.")
    }
  }

  const handleDeleteTeam = async (teamId: number) => {
    const token = localStorage.getItem("access_token")
    if (!token) return

    if (!confirm("¿Estás seguro de que quieres eliminar este equipo?")) return

    try {
      const response = await fetch(`http://localhost:8000/teams/${teamId}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      })

      if (response.ok) {
        setTeams((prev) => prev.filter((team) => team.id !== teamId))
        setStats((prev) => ({ ...prev, totalTeams: prev.totalTeams - 1 }))
      } else {
        const errorData = await response.json()
        setError(errorData.detail || "Failed to delete team")
      }
    } catch (error) {
      setError("Network error. Please try again.")
    }
  }

  const handleLogout = () => {
    localStorage.removeItem("access_token")
    setIsAuthenticated(false)
    setUser(null)
    setTeams([])
    setStats({
      totalTeams: 0,
      totalPlayers: 0,
      totalMatches: 0,
      totalTournaments: 0,
    })
  }

  if (!isAuthenticated) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-orange-50 to-red-100 flex items-center justify-center p-4">
        <Card className="w-full max-w-md">
          <CardHeader className="space-y-1">
            <div className="flex items-center justify-center mb-4">
              <div className="bg-orange-500 p-3 rounded-full">
                <BarChart3 className="h-6 w-6 text-white" />
              </div>
            </div>
            <CardTitle className="text-2xl text-center">Basketball Stats</CardTitle>
            <CardDescription className="text-center">
              Inicia sesión para acceder a tu dashboard de estadísticas de baloncesto
            </CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleLogin} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="username">Usuario</Label>
                <Input
                  id="username"
                  type="text"
                  placeholder="Ingresa tu usuario"
                  value={loginForm.username}
                  onChange={(e) => setLoginForm((prev) => ({ ...prev, username: e.target.value }))}
                  required
                />
              </div>
              <div className="space-y-2">
                <Label htmlFor="password">Contraseña</Label>
                <div className="relative">
                  <Input
                    id="password"
                    type={showPassword ? "text" : "password"}
                    placeholder="Ingresa tu contraseña"
                    value={loginForm.password}
                    onChange={(e) => setLoginForm((prev) => ({ ...prev, password: e.target.value }))}
                    required
                  />
                  <Button
                    type="button"
                    variant="ghost"
                    size="sm"
                    className="absolute right-0 top-0 h-full px-3 py-2 hover:bg-transparent"
                    onClick={() => setShowPassword(!showPassword)}
                  >
                    {showPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                  </Button>
                </div>
              </div>
              {error && (
                <Alert variant="destructive">
                  <AlertDescription>{error}</AlertDescription>
                </Alert>
              )}
              <Button type="submit" className="w-full bg-orange-500 hover:bg-orange-600" disabled={loading}>
                {loading ? (
                  <div className="flex items-center">
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                    Iniciando sesión...
                  </div>
                ) : (
                  <>
                    <LogIn className="mr-2 h-4 w-4" />
                    Iniciar Sesión
                  </>
                )}
              </Button>
            </form>
            <div className="mt-4 p-3 bg-gray-50 rounded-lg text-sm">
              <p className="font-medium mb-1">Credenciales de prueba:</p>
              <p>Admin: admin / admin123</p>
              <p>Coach: coach1 / coach123</p>
            </div>
          </CardContent>
        </Card>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center">
              <div className="bg-orange-500 p-2 rounded-lg mr-3">
                <BarChart3 className="h-6 w-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-semibold text-gray-900">Basketball Stats</h1>
                <p className="text-sm text-gray-500">Dashboard</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <div className="text-right">
                <p className="text-sm font-medium text-gray-900">{user?.full_name || user?.username}</p>
                <p className="text-xs text-gray-500">{user?.email}</p>
              </div>
              <Button variant="outline" onClick={handleLogout}>
                Cerrar Sesión
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Error Alert */}
        {error && (
          <Alert variant="destructive" className="mb-6">
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">Total Equipos</CardTitle>
              <Users className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{stats.totalTeams}</div>
              <p className="text-xs text-muted-foreground">Equipos a los que tienes acceso</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">Total Jugadores</CardTitle>
              <Users className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{stats.totalPlayers}</div>
              <p className="text-xs text-muted-foreground">Jugadores activos</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">Total Partidos</CardTitle>
              <Calendar className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{stats.totalMatches}</div>
              <p className="text-xs text-muted-foreground">Partidos jugados</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">Torneos</CardTitle>
              <Trophy className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{stats.totalTournaments}</div>
              <p className="text-xs text-muted-foreground">Torneos activos</p>
            </CardContent>
          </Card>
        </div>

        {/* Main Content Tabs */}
        <Tabs defaultValue="teams" className="space-y-4">
          <TabsList>
            <TabsTrigger value="teams">Equipos</TabsTrigger>
            <TabsTrigger value="players">Jugadores</TabsTrigger>
            <TabsTrigger value="matches">Partidos</TabsTrigger>
            <TabsTrigger value="stats">Estadísticas</TabsTrigger>
          </TabsList>

          <TabsContent value="teams" className="space-y-4">
            <Card>
              <CardHeader>
                <div className="flex justify-between items-center">
                  <div>
                    <CardTitle>Tus Equipos</CardTitle>
                    <CardDescription>Equipos que puedes ver y gestionar</CardDescription>
                  </div>
                  <Dialog open={showNewTeamDialog} onOpenChange={setShowNewTeamDialog}>
                    <DialogTrigger asChild>
                      <Button className="bg-orange-500 hover:bg-orange-600">
                        <Plus className="mr-2 h-4 w-4" />
                        Nuevo Equipo
                      </Button>
                    </DialogTrigger>
                    <DialogContent>
                      <DialogHeader>
                        <DialogTitle>Crear Nuevo Equipo</DialogTitle>
                        <DialogDescription>Ingresa los datos del nuevo equipo de baloncesto.</DialogDescription>
                      </DialogHeader>
                      <form onSubmit={handleCreateTeam} className="space-y-4">
                        <div className="space-y-2">
                          <Label htmlFor="team-name">Nombre del Equipo</Label>
                          <Input
                            id="team-name"
                            placeholder="Ej: Lakers"
                            value={newTeam.nombre}
                            onChange={(e) => setNewTeam((prev) => ({ ...prev, nombre: e.target.value }))}
                            required
                          />
                        </div>
                        <div className="space-y-2">
                          <Label htmlFor="team-city">Ciudad</Label>
                          <Input
                            id="team-city"
                            placeholder="Ej: Los Angeles"
                            value={newTeam.ciudad}
                            onChange={(e) => setNewTeam((prev) => ({ ...prev, ciudad: e.target.value }))}
                          />
                        </div>
                        <div className="flex justify-end space-x-2">
                          <Button type="button" variant="outline" onClick={() => setShowNewTeamDialog(false)}>
                            Cancelar
                          </Button>
                          <Button type="submit" className="bg-orange-500 hover:bg-orange-600">
                            Crear Equipo
                          </Button>
                        </div>
                      </form>
                    </DialogContent>
                  </Dialog>
                </div>
              </CardHeader>
              <CardContent>
                {teams.length > 0 ? (
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {teams.map((team) => (
                      <Card key={team.id} className="hover:shadow-md transition-shadow">
                        <CardHeader className="pb-3">
                          <div className="flex justify-between items-start">
                            <div>
                              <CardTitle className="text-lg">{team.nombre}</CardTitle>
                              {team.ciudad && <CardDescription>{team.ciudad}</CardDescription>}
                            </div>
                            <div className="flex space-x-1">
                              <Button variant="ghost" size="sm">
                                <Edit className="h-4 w-4" />
                              </Button>
                              <Button
                                variant="ghost"
                                size="sm"
                                onClick={() => handleDeleteTeam(team.id)}
                                className="text-red-600 hover:text-red-700"
                              >
                                <Trash2 className="h-4 w-4" />
                              </Button>
                            </div>
                          </div>
                        </CardHeader>
                        <CardContent>
                          <div className="flex justify-between items-center">
                            <Badge variant="secondary">Equipo #{team.id}</Badge>
                            <Button variant="outline" size="sm">
                              Ver Detalles
                            </Button>
                          </div>
                        </CardContent>
                      </Card>
                    ))}
                  </div>
                ) : (
                  <div className="text-center py-8">
                    <Users className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                    <h3 className="text-lg font-medium text-gray-900 mb-2">No se encontraron equipos</h3>
                    <p className="text-gray-500 mb-4">Aún no tienes acceso a ningún equipo.</p>
                    <Button onClick={() => setShowNewTeamDialog(true)} className="bg-orange-500 hover:bg-orange-600">
                      <Plus className="mr-2 h-4 w-4" />
                      Crear Primer Equipo
                    </Button>
                  </div>
                )}
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="players" className="space-y-4">
            <Card>
              <CardHeader>
                <CardTitle>Jugadores</CardTitle>
                <CardDescription>Estadísticas e información de jugadores</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="text-center py-8">
                  <Users className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                  <h3 className="text-lg font-medium text-gray-900 mb-2">Sección de Jugadores</h3>
                  <p className="text-gray-500">Las funciones de gestión de jugadores estarán disponibles pronto.</p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="matches" className="space-y-4">
            <Card>
              <CardHeader>
                <CardTitle>Partidos</CardTitle>
                <CardDescription>Resultados y calendarios de partidos</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="text-center py-8">
                  <Calendar className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                  <h3 className="text-lg font-medium text-gray-900 mb-2">Sección de Partidos</h3>
                  <p className="text-gray-500">Las funciones de gestión de partidos estarán disponibles pronto.</p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="stats" className="space-y-4">
            <Card>
              <CardHeader>
                <CardTitle>Estadísticas</CardTitle>
                <CardDescription>Estadísticas avanzadas y análisis de baloncesto</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="text-center py-8">
                  <BarChart3 className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                  <h3 className="text-lg font-medium text-gray-900 mb-2">Sección de Estadísticas</h3>
                  <p className="text-gray-500">Las funciones de estadísticas avanzadas estarán disponibles pronto.</p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </main>
    </div>
  )
}
